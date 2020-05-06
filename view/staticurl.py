
from tornado.web import RequestHandler as requesthandler


#staticurl handler
class staticurlHandler(requesthandler):
    def get(self):
        data=dict(
            cardTitle="See the world with Statistic url"
        )
        self.render("staticurl.html",data=data)
