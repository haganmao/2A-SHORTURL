import hashlib
import tornado.web
import datetime
import os


from tornado.web import RequestHandler as requesthandler
from wtforms import Form, StringField
from wtforms.validators import DataRequired, URL




# core Handler
class coreHandler(requesthandler):
    # get the shortcode from codemap
    def getCode(self, originalUrl):
        shortCode = []
        for code in range(97, 123):
            if (code == 105 or code == 106 or code == 108 or code == 111):
                continue
            shortCode.append(chr(code))
        for code in range(0, 10):
            if (code == 0):
                continue
            shortCode.append(str(code))
        for code in range(65, 91):
            if (code == 73 or code == 79):
                continue
            shortCode.append(chr(code))
        shortCode = tuple(shortCode)
        # return shortCode, len(shortCode)

        # get the md5 str for originalurl
        originalMd5 = self.getMd5(originalUrl)

        # The final options for code list
        code = []
        # slice the Md5 to 4 pieces
        for i in range(0, 4):
            p = int(originalMd5[i * 8:(i + 1) * 8], 16)
            shortCodeList = []
            # for loop 5 times to get each option of shortCodeList
            for j in range(0, 5):
                k = 0x00000036 & p
                shortCodeList.insert(0, shortCode[k][::-1])
                p = p >> 6
            code.append(''.join(shortCodeList))
        return code


    # get md5 for long url
    def getMd5(self, originalUrl):
        hl = hashlib.md5()
        hl.update(originalUrl.encode(encoding='utf-8'))
        return hl.hexdigest()
        # return hl.hexdigest(), len(hl.hexdigest())


    #get current datetime 
    def getDay(self, day=0):
        return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime("%Y-%m-%d")

    # get last 7 days list
    def getDay_list_7(self,daynow):
        for i in range(1, 8):
            oneday = datetime.timedelta(days=i)
            day = daynow - oneday
            date_to = datetime.datetime(day.year, day.month, day.day)
            yield str(date_to)[6:10]


    # get form Params
    @property
    def getFormData(self):
        formparams = self.request.arguments
        formparams = {
            item[0]:list(
                map(
                    lambda params: str(params, encoding='utf-8'),
                    item[1]
                )
            )
            for item in formparams.items()
        }
        return formparams
    
    # get the new session
    @property
    def session(self):
        return self.application.db

    
    @property
    #get create time
    def getCreateTime(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    #get server ip address
    def gerIP(self):
        return "http://2a.nz/"

     

# form validator
class urlForm(Form):
    url = StringField(
        'url',
        validators=[
            DataRequired(
                'Please check your link and try again, url must be filled'),
            URL(message='is not a valid url, Unable to shorten that link, Enter exp:http://..or https://..')
        ]
    )

