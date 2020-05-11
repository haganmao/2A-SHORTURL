from view.core import coreHandler
from model.database import ShortUrlInfo, ShorturlOverview


#302 redirect to longurl and save as records
class redirectHandler(coreHandler):
    def get(self, scode):
        try:
            # get the object from db, sqlachemy
            # print("################8")
            shortcode = self.session.query(ShortUrlInfo).filter_by(short_code=scode).first()
            print("########################7")
            print(shortcode.short_code)
            print(shortcode.id)
            print(shortcode.original_url)

            #save access record
            self.save_record(shortcode.id)
            print("########################8")
        except Exception as exception:
            self.session.rollback()
            
        else:
            self.session.commit()
        finally:
            self.session.close()
            print("###########################11")
        self.redirect(shortcode.original_url)

    #save overview record, write data to databases
    def save_record(self,sid):
        print('############################getlocation')
        print(self.request.remote_ip)
    
        try:
            print("######################9")
            Shorturl_Overview = ShorturlOverview(
                short_url_id = sid,
                short_url = self.request.uri[1:],
                short_url_requestIP = self.request.remote_ip,
                short_url_requestMethod = self.request.method,
                short_url_requestLocation = '127.0.0.1',
                short_url_createTime = self.getCreateTime
            )
            self.session.add(Shorturl_Overview)
            print("######################10")
            print(Shorturl_Overview.short_url_requestIP)
            print(Shorturl_Overview.short_url)
            print(Shorturl_Overview.short_url_id)
            print(Shorturl_Overview.short_url_requestMethod)
            # print(Shorturl_Overview.short_url_requestLocation)
            print(Shorturl_Overview.short_url_createTime)
        except Exception as exception:
            self.session.rollback()
            
        else:
            self.session.commit()
        finally:
            self.session.close()

