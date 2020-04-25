
from tornado.web import RequestHandler as requesthandler



#Home handler
class ErrorHandler(requesthandler):
    def get(self):
        self.render("error404.html")