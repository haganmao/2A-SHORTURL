from view.core import coreHandler
# from tornado.web import RequestHandler as requesthandler #import RequestHandler class
from model.database import ShortUrlInfo

# Overview handler


class overviewHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle="DO YOU KNOW RESULT?"
        )
        print("###############################1")
        uu_id = self.get_argument('uuid', None)
        print(uu_id)
        print("###############################")
        if uu_id:
            try:
                uuid = self.session.query(ShortUrlInfo).filter_by(
                    uuid=uu_id
                ).first()
                data['uuid'] = uuid
                print('###############################2')
            except Exception as exception:
                self.session.rollback()
            else:
                self.session.commit()
            finally:
                self.session.close()
            self.render("overview.html", data=data)
    
        
