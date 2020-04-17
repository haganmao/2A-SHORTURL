import template
from tornado.web import RequestHandler as requesthandler



#Home handler, rendering html pages
class HomeHandler(requesthandler):
     def get (self):
         self.render("home.html")


