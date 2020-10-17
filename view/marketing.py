
from view.core import coreHandler 


class marketingHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle = ""
        )
        self.render('marketing.html', data = data)


