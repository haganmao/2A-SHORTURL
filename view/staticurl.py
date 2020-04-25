
from tornado.web import RequestHandler as requesthandler


#staticurl handler
class staticurlHandler(requesthandler):
    def get(self):
        self.render("staticurl.html")