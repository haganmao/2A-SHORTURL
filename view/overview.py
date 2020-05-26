from view.core import coreHandler
# from tornado.web import RequestHandler as requesthandler #import RequestHandler class
from model.database import ShortUrlInfo, ShorturlOverview
from sqlalchemy import and_

# Overview handler
class overviewHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle="Generated URL"
        )
        # print("###############################1")
        # get the uuid
        uu_id = self.get_argument('uuid', None)
        # print(uu_id)
        # print("###############################")

        if uu_id:
            try:
                #get the uuid from database
                uuid = self.session.query(ShortUrlInfo).filter_by(
                    uuid=uu_id
                ).first()

        
                #get shortcode and longurl
                data['scode'] = uuid.short_code
                data['longurl'] = uuid.original_url

                # print("#########################DV0")
                # print(ShorturlOverview.short_url_id)
                # print(uuid.id)
                
                #count the numbers of day vistor
                data['day_visitor'] = self.session.query(ShorturlOverview).filter(
                    and_(
                        ShorturlOverview.short_url_id == uuid.id,
                        ShorturlOverview.short_url_createTime >= self.getDay() + " 00:00:00",
                        ShorturlOverview.short_url_createTime < self.getDay(
                            1) + " 00:00:00"
                    )
                ).count()
                # print("##########################DV_dvis")
                # print(data['day_visitor'])

                data['total_vistor'] = self.session.query(ShorturlOverview).filter_by(
                    short_url_id=uuid.id
                ).count()

                # print("##########################DV_dtis")
                # print(data['total_vistor'])

                data['uuid'] = uuid
                # print('###############################2')
            except Exception as exception:
                self.session.rollback()
            else:
                self.session.commit()
            finally:
                self.session.close()
            self.render("overview.html", data=data)

    # To response ShorturlOverview info from ajax http post request in overview page
    def post(self):

        # status code 200:success 500:fail
        result = dict(statuscode=500)
        pageNumber = int(self.get_argument('pageNumber', 1))
        uuid = self.get_argument('uuid', None)
        try:
            dataNum = 5
            dataInfo = self.session.query(ShortUrlInfo, ShorturlOverview).filter(
                and_(
                    ShortUrlInfo.uuid == uuid,
                    ShorturlOverview.short_url_id == ShortUrlInfo.id
                )
            ).offset((pageNumber-1) * dataNum).limit(dataNum)
            
            # print("################datainfo")
            
            result['datainfo'] = []
            for d in dataInfo:
                obj = dict(
                    id=d.ShorturlOverview.id,
                    short_url=d.ShorturlOverview.short_url,
                    short_url_requestIP=d.ShorturlOverview.short_url_requestIP,
                    short_url_requestLocation=d.ShorturlOverview.short_url_requestLocation,
                    short_url_requestMethod=d.ShorturlOverview.short_url_requestMethod,
                    short_url_createTime=d.ShorturlOverview.short_url_createTime.strftime("%Y-%m-%d %H:%M:%S")
                )
                result['datainfo'].append(obj)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # print(result['datainfo'])
            if result["datainfo"]:
                result["statuscode"] = 200
            else:
                result["statuscode"] = 500
        except Exception as exception:
            self.session.rollback()
        else:
            self.session.commit()
        finally:
            self.session.close()
        self.write(result)
