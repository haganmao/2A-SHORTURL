import tornado.web
import config
import pymysql
from tornado.template import Loader

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
from view.contact import contactHandler as contact
from view.b2b import b2bHandler as b2b
from view.socialmedia import socialmediaHandler as socialmedia
from view.sms import smsHandler as sms
from view.policy import policylHandler as policy
from view.term import termHandler as term
from view.worldmap import worldmapHandler as worldmap
from view.pie import pieHandler as pie
from view.calendar import calendarHandler as calendar


# mapping between view and router
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", home),
            (r"/overview", overview),
            (r"/([a-zA-Z0-9]{5})", redirect),
            (r"/test",test),
            (r"/worldmap",worldmap),
            (r"/pie",pie),
            (r"/calendar",calendar),
            # (r"/codemap", core),
            (r"/static", staticurl),
            (r"/b2b", b2b),
            (r"/socialmedia", socialmedia),
            (r"/sms", sms),
            (r"/contact",contact),
            (r"/policy",policy),
            (r"/term",term),
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
