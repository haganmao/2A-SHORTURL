
from tornado.web import RequestHandler as requesthandler



#Home handler
class HomeHandler(requesthandler):
     def get (self):
         data = dict(
             cardTitle = "Try 2a Short Url Provider, You'll Like It"
         )
         self.render("home.html", data=data)


