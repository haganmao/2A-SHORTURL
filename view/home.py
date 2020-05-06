import uuid

from view.core import coreHandler
from werkzeug.datastructures import MultiDict
from wtforms import Form, StringField
from wtforms.validators import DataRequired, URL
from model.database import ShortUrlInfo

# form validator
class urlForm(Form):
    url = StringField(
        'url',
        validators=[
            DataRequired(
                'Please check your link and try again, url must be filled'),
            URL(message='Unable to shorten that link. It is not a valid url, exp:http://..or https://..')
        ]
    )

# Home handler
class HomeHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle="Try 2a Short Url Provider, You'll Like It"
        )
        self.render("home.html", data=data)

    def post(self):
        # status code 1:success 0:fail
        result = dict(res=0)
        urlform = urlForm(MultiDict(self.getFormData))
        # print("************************************************")
        # print(urlform.data["url"])

        if urlform.validate():
            # check the original_url is exist on database or not, if not save the data to database
            print(self.session)
            # print("###############")
            try:
                long_url = self.session.query(ShortUrlInfo).filter_by(
                    original_url=urlform.data['url']
                ).first()
                print(long_url)
                # print("###############1")
                uu_id = uuid.uuid4().hex
                short_code = self.getCode(urlform.data['url'])[0]
                if not long_url:
                    shorturlinfo = ShortUrlInfo(
                        original_url=urlform.data['url'],
                        short_code=short_code,
                        uuid=uu_id,
                        create_time=self.getCreateTime()
                    )
                    # print("#################2")
                    self.session.add(shorturlinfo)
                else:
                    uu_id = long_url.uuid
                result['res'] = 1
                result['uuid'] = uu_id
            except Exception as e:
                self.session.rollback()
            else:
                self.session.commit()
            finally:
                self.session.close()
        else:
            result = urlform.errors
            result['res'] = 0
        self.write(result)
