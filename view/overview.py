
from tornado.web import RequestHandler as requesthandler #import RequestHandler class

#Overview handler
class overviewHandler(requesthandler):
    def get(self):
        data = dict(
            cardTitle="DO YOU KNOW RESULT?"
        )
        self.render("overview.html", data=data)
