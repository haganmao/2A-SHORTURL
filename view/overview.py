import tornado.web #import tornado web library
from tornado.web import RequestHandler as requesthandler #import RequestHandler class

#Overview handler, rendering html pages
class overviewHandler(requesthandler):
    def get(self):
        data = dict(
            cardTitle="This is overview page"
        )
        self.render("overview.html", data=data)
