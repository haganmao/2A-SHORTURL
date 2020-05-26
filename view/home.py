import uuid
import time
from view.core import coreHandler, urlForm
from model.database import ShortUrlInfo
from werkzeug.datastructures import MultiDict

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
        # print("************************************************")
        # print(urlform.data["url"])

        if urlform.validate():
            # check the original_url is exist on database or not, if not save the data to database
            # print(self.session)
            # print("###############")
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            t = time.time()
            # print(t)
            # print(urlform.data['url'] + str(int(round(t*1000))))
            try:
                uu_id = uuid.uuid4().hex
                short_codes = self.getCode(str(int(round(t*1000))) + urlform.data['url'])
                # print("!~~~~~~~~~~~~~~~~~~~~~~~~~~")
                # print(str(int(round(t*1000))) + urlform.data['url'])
                # print('!!!!!!!!!!!!!!!!!!!!!shortcodes')
                # print(short_codes)
                short_code1 = short_codes[0]
                short_code2 = short_codes[1]
                short_code3 = short_codes[2]
                short_code4 = short_codes[3]

                # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                # print(short_code)
                # get the object from db, sqlachemy
                short_url = self.session.query(ShortUrlInfo).filter_by(
                    short_code=short_code1
                ).first()
                # print(long_url)
                # print("###############1")
                # if not exist, write data to database
                if not short_url:
                    shorturlinfo = ShortUrlInfo(
                        original_url=urlform.data['url'],
                        short_code=short_code1,
                        uuid=uu_id,
                        create_time=self.getCreateTime
                    )
                    # print("#################shorturlinfo")
                    # print(shorturlinfo.original_url)
                    self.session.add(shorturlinfo)
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
                        # print("#################shorturlinfo")
                        # print(shorturlinfo.original_url)
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
                            # print("#################shorturlinfo")
                            # print(shorturlinfo.original_url)
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
                                # print("#################shorturlinfo")
                                # print(shorturlinfo.original_url)
                                self.session.add(shorturlinfo)
                            else:
                                result = urlform.errors
                                result['statuscode'] = 500
                                result['url'] = 'shorturl occupied'
                                # self.write(result['statuscode'])
                                # self.write(result['url'])
                                self.write(result)
                                return
                result['statuscode'] = 200
                result['uuid'] = uu_id
                # r=result['uuid']
                # print("#################1")
                # print(result)
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
