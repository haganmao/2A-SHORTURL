from view.core import coreHandler
from model.database import ShortUrlInfo, ShorturlOverview
from view.ip2location import getIpLocation

# 302 redirect to longurl and save as records
class redirectHandler(coreHandler):
    def get(self, scode):
        try:
            # get the object from db, sqlachemy
            # print("################8")
            shortcode = self.session.query(ShortUrlInfo).filter_by(short_code=scode).first()
            self.save_overview_info(shortcode.id)
        except Exception as exception:
            self.session.rollback()
        else:
            self.session.commit()
        finally:
            self.session.close()
        # print("###########################longurl1")
        # print(shortcode.original_url)
        # print("###########################uuid2")
        # print(shortcode.uuid)
        # print("#################id")
        # print(shortcode.id)
        self.redirect(shortcode.original_url)

    #save overview record, write data to databases
    def save_overview_info(self, short_url_id):
        try:
            saveoverview_info = ShorturlOverview(
                short_url_id = short_url_id,
                short_url = self.request.uri[1:],
                short_url_requestIP = self.request.remote_ip,
                short_url_requestLocation = getIpLocation(self.request.remote_ip)['region'],
                short_url_requestMethod = self.request.method,
                short_url_createTime = self.getCreateTime
            )
            self.session.add(saveoverview_info)
        except Exception as exception:
            self.session.rollback()
        else:
            self.session.commit()
        finally:
            self.session.close()
   

