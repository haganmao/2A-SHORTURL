import tornado.web
from tornado.web import RequestHandler as requesthandler


#staticurl handler, rendering html pages
class staticurlHandler(requesthandler):
    def get(self):
        self.render("staticurl.html")