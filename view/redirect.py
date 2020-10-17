import urllib
from urllib import request
import json
import redis

from view.core import coreHandler
from model.database import ShortUrlInfo, ShorturlOverview
from tool.geoIp2 import getAddr
from config import redis_db

#302 redirect to longurl and save as records
class redirectHandler(coreHandler):
    def get(self, scode):
       
        try:
            r = redis.Redis(host=redis_db['redis_host'], port=redis_db['redis_port'], db=redis_db['redis_db'])
            ret = r.get(scode)
            if(ret is None):
                self.render("error404.html")
                return
            # get the object from db, sqlachemy
            shortcode = self.session.query(ShortUrlInfo).filter_by(short_code=scode).first()

            #save access record
           #self.save_record(shortcode.id)
        except Exception as exception:
            self.session.rollback()
            
        else:
            self.session.commit()
        finally:
            self.session.close()
        self.redirect(shortcode.original_url)
        self.save_record(shortcode.id)
    #using stringuseragent api to get user agent info with json format
    def getUserAgent(self,ua): 
        #URL encode for a valid ua
        ua_url = urllib.parse.quote(ua)
        url = "http://www.useragentstring.com/?uas=%s&getJSON=all" %ua_url

        #construct a completed request
        req = urllib.request.Request(url)

        #read response and loadind with json
        res = urllib.request.urlopen(req).read()
        res = json.loads(res)
        return res
    
    # isMobile = 'you are not mobile' if ua.find('Mobile') == -1 else 'you are mobile'
    def checkConnectType(self,ua):
        if ua.find('Mobile')== -1:
            connectType = 'PC'
            return connectType

        else:
            connectType = 'Mobile'
            return connectType


    #save overview record, write data to databases
    def save_record(self,sid):
        
        # get headers info exp client devece info,broswer etc
        ua = self.request.headers['User-Agent']
        uainfo = self.getUserAgent(ua)
        connectType = self.checkConnectType(ua)

        try:
            location = getAddr(self.request.remote_ip)
            if location['find'] == 1:
                Shorturl_Overview = ShorturlOverview(
                    short_url_id = sid,
                    short_url = self.request.uri[1:],
                    short_url_requestIP = self.request.remote_ip,
                    short_url_requestLocation = location['addr'],
                    short_url_requestMethod = self.request.method,
                    short_url_requesCountry =  location['response_contury'],
                    short_url_createTime = self.getCreateTime,
                    short_url_access_osType = uainfo['os_type'],
                    short_url_access_osName = uainfo['os_name'],
                    short_url_access_agent_name = uainfo['agent_name'],
                    short_url_access_connectType = connectType
                )
                self.session.add(Shorturl_Overview)
            else:
                Shorturl_Overview = ShorturlOverview(
                    short_url_id = sid,
                    short_url = self.request.uri[1:],
                    short_url_requestIP = self.request.remote_ip,
                    short_url_requestLocation = location['addr'],
                    short_url_requestMethod = self.request.method,
                    short_url_createTime = self.getCreateTime,
                    short_url_access_osType = uainfo['os_type'],
                    short_url_access_osName = uainfo['os_name'],
                    short_url_access_agent_name = ['agent_name'],
                    short_url_access_connectType = connectType
                )
                self.session.add(Shorturl_Overview)
        except Exception as exception:
            self.session.rollback()
        else:
            self.session.commit()
        finally:
            self.session.close()
        
