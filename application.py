import tornado.web
import config

from view.home import HomeHandler as home
from view.overview import overviewHandler as overview 
from view.staticurl import staticurlHandler as staticurl 
from view.error404 import ErrorHandler as error
from view.core import codemapHandler as codemap

#mapping between view and router 
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", home),
            (r"/codemap", codemap),
            (r"/overview",overview),
            (r"/static", staticurl),
            (r"/.*",error)
        ]
        super(Application,self).__init__(handlers,**config.settings)