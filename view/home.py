import template
from tornado.web import RequestHandler as requesthandler



#Home handler, rendering html pages
class HomeHandler(requesthandler):
     def get (self):
         data = dict(
             cardTitle = "Try 2a Short Url Provider, You'll Like It"
         )
         self.render("home.html", data=data)


