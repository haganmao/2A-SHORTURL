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
        # shortCode1 = (
        #     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        #     'k', 'm', 'n', 'p', 'q', 'r', 's', 't',
        #     'u', 'v', 'w', 'x', 'y', 'z', '1', '2',
        #     '3', '4', '5', '6', '7', '8', '9', 'A',
        #     'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
        #     'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
        #     'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        # )

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
                # print(shortCode[k])
            code.append(''.join(shortCodeList))
        return code

        # p0 = int(originalMd5[0*8:(0+1)*8],16)
        # p1 = originalMd5[1*8:(1+1)*8]
        # p2 = int(originalMd5[2*8:(2+1)*8],16)
        # p3 = int(originalMd5[3*8:(3+1)*8],16)
        # return p0,p1,p2,p3

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

    # get last 14 days list
    # def getDay_list_14(self,daynow):
    #     for i in range(1, 15):
    #         oneday = datetime.timedelta(days=i)
    #         day = daynow - oneday
    #         date_to = datetime.datetime(day.year, day.month, day.day)
    #         yield str(date_to)[6:10]

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
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxpa")
        print(formparams)
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
        return "http://127.0.0.1:8080/"

     

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

