import tornado.web
import config



from view.home import HomeHandler as home
from view.overview import overviewHandler as overview 
from view.staticurl import staticurlHandler as staticurl 
from view.error404 import ErrorHandler as error
from view.core import coreHandler as core
from sqlalchemy import create_engine
from config import mysql_db
from sqlalchemy.orm import sessionmaker


#mapping between view and router 
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", home),
            (r"/codemap", core),
            (r"/overview",overview),
            (r"/static", staticurl),
            (r"/.*",error)
        ]
        super(Application,self).__init__(handlers,**config.settings)
    
    @property
    def createDBSession(self):
        # create an new engine for connecting to shorturl_2A, and formatting the connector url
        engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            mysql_db["admin"],
            mysql_db["password"],
            mysql_db["host"],
            mysql_db["port"],
            mysql_db["dbname"]
            ),  
            #echo set to true, print the create processing
            echo =True,
            encoding="utf-8",
            pool_size=0
        )

        dbSession = sessionmaker(
            bind=engine,
            autoflush=True,
            autocommit=False,
            expire_on_commit=True
        )
        return dbSession()
