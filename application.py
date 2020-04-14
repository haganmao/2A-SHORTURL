import tornado.web
import config

from view.home import HomeHandler as home
# from view.index import JsonHandler as json
from view.overview import overviewHandler as overview 
from view.staticurl import staticurlHandler as staticurl 


#router setup
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", home),      
            (r"/overview",overview),
            (r"/static", staticurl)
        ]
        super(Application,self).__init__(handlers,**config.settings)