import tornado.web
import config

from view.home import HomeHandler as home
# from view.index import JsonHandler as json

#router setup
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", home)      
        ]
        super(Application,self).__init__(handlers,**config.settings)