
import uuid
from view.core import coreHandler
from view.core import urlForm,MultiDict
from model.database import ShortUrlInfo


# Home handler
class HomeHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle="Try 2a Short Url Provider, You'll Like It"
        )
        self.render("home.html", data=data)

    
    def post(self):
        #status code 1:success 0:fail
        result = dict(res=0)
        formData = self.getFormData
        urlform = urlForm(MultiDict(formData))
        print("#################")
        print(formData['url'])
        if urlform.validate():
            #check the original_url is exist on database or not, if not save the data to database
            try:
                print("#@###################")
                print(formData['url'][0])
                long_url = self.session.query(ShortUrlInfo).filter_by(
                    original_url = formData['url'][0]
                ).first()
                
                if not long_url:
                    print("ppppp")
                    uuid = uuid.uuid4().hex
                    print("xxxxxxxxx")
                    shorturlinfo = ShortUrlInfo(
                       original_url = formData['url'][0],
                       short_code = self.getCode(formData['url'][0])[0],
                       uuid = uuid,
                       create_time = self.getCreateTime()
                    )
                    print("#########################")
                    print(shorturlinfo)
                    self.session.add(shorturlinfo)
                else:
                    print("nnnnnnnnnnn")
                    uuid = long_url.uuid
                result['res'] = 1
                result['uuid'] = uuid
            except Exception as exception:
                self.session.rollback()
            else:
                self.session.commit()
            finally:
                self.session.close()
        else:
            result = urlform.errors
            result['res'] = 0
        self.write(result)

  