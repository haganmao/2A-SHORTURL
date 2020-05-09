import uuid

from view.core import coreHandler,urlForm
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
            print(self.session)
            # print("###############")
            try:
                ##get the object from db, sqlachemy
                long_url = self.session.query(ShortUrlInfo).filter_by(
                    original_url=urlform.data['url']
                ).first()
                # print(long_url)
                # print("###############1")
                uu_id = uuid.uuid4().hex
                short_code = self.getCode(urlform.data['url'])[0]
                #if not exist, write data to database
                if not long_url:
                    shorturlinfo = ShortUrlInfo(
                        original_url=urlform.data['url'],
                        short_code=short_code,
                        uuid=uu_id,
                        create_time=self.getCreateTime
                    )
                    # print("#################shorturlinfo")
                    # print(shorturlinfo.original_url)
                    self.session.add(shorturlinfo)
                else:
                    uu_id = long_url.uuid
                result['statuscode'] = 200
                result['uuid'] = uu_id
                # r=result['uuid']
                print("#################1")
                print(result)
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
