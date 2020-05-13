import tornado.web
import config
import pymysql


from view.home import HomeHandler as home
from view.overview import overviewHandler as overview
from view.staticurl import staticurlHandler as staticurl
from view.error404 import ErrorHandler as error
from view.core import coreHandler as core
from view.redirect import redirectHandler as redirect
from sqlalchemy import create_engine
from config import mysql_db
from sqlalchemy.orm import sessionmaker
from view.getMd5test import testHandler as test

# mapping between view and router
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", home),
            (r"/overview", overview),
            (r"/([a-zA-Z0-9]{5})", redirect),
            (r"/test",test),
            # (r"/codemap", core),
            (r"/static", staticurl),
            (r"/.*", error)
        ]
        self.db = self.createDBSession
        super(Application, self).__init__(handlers, **config.settings)

   
    # create new session
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
            # echo set to true, print the create processing
            encoding="utf-8",
            echo=True,
            pool_size=100,
            pool_recycle=10,
            connect_args={"charset": 'utf8'}
        )

        # bind engine
        dbSession = sessionmaker(
            bind=engine,
            autoflush=True,
            autocommit=False,
            expire_on_commit=False
        )
        #return an new dbsession with parameters
        return dbSession()
