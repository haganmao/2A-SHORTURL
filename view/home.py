import template
import json

from tornado.web import RequestHandler



#Index handler, rendering html pages
class HomeHandler(RequestHandler):
     def get (self):
         self.render("home.html")


