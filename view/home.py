import uuid
import time
import redis
from view.core import coreHandler, urlForm
from model.database import ShortUrlInfo
from werkzeug.datastructures import MultiDict
from config import redis_db


# Home handler
class HomeHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle="Try 2a Short Url Provider, You'll Like It"
        )
        self.render("home.html", data=data)

    def post(self):
        # status code 200:success 500:fail
        result = dict(statuscode=500)
        urlform = urlForm(MultiDict(self.getFormData))
       

        if urlform.validate():
            # check the original_url is exist on database or not, if not save the data to database
            t = time.time()
          
            try:
                uu_id = uuid.uuid4().hex
                short_codes = self.getCode(str(int(round(t*1000))) + urlform.data['url'])
                
                short_code1 = short_codes[0]
                short_code2 = short_codes[1]
                short_code3 = short_codes[2]
                short_code4 = short_codes[3]

           
                # get the object from db, sqlachemy
                short_url = self.session.query(ShortUrlInfo).filter_by(
                    short_code=short_code1
                ).first()
              
                # if not exist, write data to database
                if not short_url:
                    shorturlinfo = ShortUrlInfo(
                        original_url=urlform.data['url'],
                        short_code=short_code1,
                        uuid=uu_id,
                        create_time=self.getCreateTime
                    )
                  
                    # redis-server.exe redis.windows.conf start redis service command
                    # redis-cli.exe -h 127.0.0.1 -p 6379 start redis command
                    self.session.add(shorturlinfo)
                    r = redis.Redis(host=redis_db['redis_host'], port=redis_db['redis_port'], db=redis_db['redis_db'])
                    ret = r.set(short_code1, urlform.data['url'])
                  
                    if self.getFormData["expireTime"][0]=="1":
                        r.expire(short_code1, 60*60*24) 
                    elif self.getFormData["expireTime"][0]=="2":
                        r.expire(short_code1, 60*60*24*7)
                    elif self.getFormData["expireTime"][0]=="3":
                        r.expire(short_code1, 60*60*12*365*100) 
                else:
                    short_url = self.session.query(ShortUrlInfo).filter_by(
                        short_code=short_code2
                    ).first()
                    if not short_url:
                        shorturlinfo = ShortUrlInfo(
                            original_url=urlform.data['url'],
                            short_code=short_code2,
                            uuid=uu_id,
                            create_time=self.getCreateTime
                        )
                        self.session.add(shorturlinfo)

                    else:
                        short_url = self.session.query(ShortUrlInfo).filter_by(
                            short_code=short_code3
                        ).first()
                        if not short_url:
                            shorturlinfo = ShortUrlInfo(
                                original_url=urlform.data['url'],
                                short_code=short_code3,
                                uuid=uu_id,
                                create_time=self.getCreateTime
                            )
                            self.session.add(shorturlinfo)
                        else:
                            short_url = self.session.query(ShortUrlInfo).filter_by(
                                short_code=short_code4
                            ).first()
                            if not short_url:
                                shorturlinfo = ShortUrlInfo(
                                    original_url=urlform.data['url'],
                                    short_code=short_code4,
                                    uuid=uu_id,
                                    create_time=self.getCreateTime
                                )
                                self.session.add(shorturlinfo)
                            else:
                                result = urlform.errors
                                result['statuscode'] = 500
                                result['url'] = 'shorturl occupied'
                                self.write(result)
                                return
                result['statuscode'] = 200
                result['uuid'] = uu_id
            except Exception as exception:
                self.session.rollback()
            else:
                self.session.commit()
            finally:
                self.session.close()
        else:
            result = urlform.errors
            result['statuscode'] = 500
        self.write(result)
