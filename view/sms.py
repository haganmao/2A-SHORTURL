
from view.core import coreHandler


class smsHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle=''
        )
        self.render('sms.html', data=data)
