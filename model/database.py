# using declarative_bas methond to create new data model
from sqlalchemy.ext.declarative import declarative_base

# import MySql field types and Column class
from sqlalchemy import Column, CHAR, VARCHAR, DATETIME, INT, BIGINT


# import mysql engine connector
from sqlalchemy import create_engine


#define a new declarativeBase, all models should be inherited the declarative_base() class, the new table and mapper will be generated.
declarativeBase = declarative_base()




# 1.Shorturl info model
# """
# 1.id: BIGINT,primarykey,auto increment
# 2.original_url:VARCHAR,unique,NOTNULL
# 3.short_code:CHAR,uniuqe,NOTNULL
# 4.uuid: CHAR,univerally unique identifier,NOTNULL
# 5.create_time: DATATIME,NOTNULL
# """


class ShortUrlInfo(declarativeBase):
    __tablename__ = 'shorturlinfo'
    id = Column(BIGINT, primary_key=True)
    original_url = Column(VARCHAR(768), unique=False, nullable=False)
    short_code = Column(CHAR(6), unique=True, nullable=False)
    uuid = Column(CHAR(32), unique=True, nullable=False)
    create_time = Column(DATETIME, nullable=False)


# access the new table name and mapper
# print("#######################")
# print(ShortUrlInfo.__tablename__)
# print(ShortUrlInfo.__mapper__)


# 2.overview info model
# """
# 1.id: BIGINT,primarykey,auto increment
# 2.short_url_id:foreignkey,BIGINT,NOTNULL
# 3.short_url_code:CHAR,NOTNULL
# 4.short_url_requestIP: CHAR
# 5.short_url_requestLocation: CHAR
# 6.short_url_requestMethod: CHAR,NOTNULL
# 7.short_url_createTime: DATETIME,NOTNULL
# 8.short_url_access_osType:CHAR,NOTNULL
# 9.short_url_access_osName:CHAR,NOTNULL
# 10.short_url_access_agent_name:CHAR,NOTNULL
# 11.short_url_access_connectType:CHAR,NOTNULL
# """

class ShorturlOverview(declarativeBase):
    __tablename__ = 'shorturloverview'
    id = Column(BIGINT, primary_key=True)
    short_url_id = Column(BIGINT, nullable=False)
    short_url = Column(VARCHAR(768), nullable=False)
    short_url_requestIP = Column(VARCHAR(128))
    short_url_requestLocation = Column(VARCHAR(300))
    short_url_requestMethod = Column(VARCHAR(30), nullable=False)
    short_url_createTime = Column(DATETIME, nullable=False)
    short_url_access_osType = Column(VARCHAR(30))
    short_url_access_osName = Column(VARCHAR(30))
    short_url_access_agent_name = Column(VARCHAR(30))
    short_url_access_connectType = Column(VARCHAR(30))
    short_url_requesCountry = Column(VARCHAR(45))

if __name__ == "__main__":
    # define mysql_db config
    mysql_db = dict(
        host="127.0.0.1",
        dbname="shorturl_2A",
        port=3306,
        admin="root",
        password="root"
    )

    # create an new engine for connecting to shorturl_2A, and formatting the connector url
    engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
        mysql_db["admin"],
        mysql_db["password"],
        mysql_db["host"],
        mysql_db["port"],
        mysql_db["dbname"]
        ),
        
        #echo set to true, print the create processing
        encoding="utf-8",
        echo=True
    )

    
    #metadata mapping model to database
    declarativeBase.metadata.create_all(engine)
    print("DB Created success!")

    




