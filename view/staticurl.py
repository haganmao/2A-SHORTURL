
import datetime
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from urllib import request
from view.core import coreHandler
from model.database import ShortUrlInfo, ShorturlOverview
from werkzeug.datastructures import MultiDict
from sqlalchemy import and_, join, func, desc, not_
from matplotlib.ticker import Formatter
from matplotlib.pyplot import MultipleLocator

# staticurl handler
class staticurlHandler(coreHandler):
    def get(self):
        uu_id = self.get_argument('uuid', None)
        uuid = self.session.query(ShortUrlInfo).filter_by(
            uuid=uu_id
        ).first()

        data = dict(
            title="See the world with Statistic url"
        )
        
        data['hCountry'] = 'no data'
        data['hIP'] = 'no data'
        data['hIP1'] = 'no data'
        data['hIP2'] = 'no data'
        data['hIP3'] = 'no data'
        data['hIP4'] = 'no data'
        data['hIP5'] = 'no data'
        data['hCountry1'] = 'no data'
        data['hCountry2'] = 'no data'
        data['hCountry3'] = 'no data'

        # get higest clicks of ip
        hIP = self.session.query((ShorturlOverview.short_url_requestIP).label('ip'), func.count(ShorturlOverview.short_url_id).label('id')).filter(
            ShorturlOverview.short_url == ShortUrlInfo.short_code).filter(ShortUrlInfo.uuid == uu_id).group_by('ip').order_by(desc('id')).limit(5).all()
        # get all access data group by date
        accesslist = self.session.query(func.date_format(ShorturlOverview.short_url_createTime, '%Y-%m-%d').label(
            'date'), func.count(ShorturlOverview.short_url_id)).filter(ShorturlOverview.short_url == ShortUrlInfo.short_code).filter(ShortUrlInfo.uuid == uu_id).group_by('date').all()
        # get highest country clicks
        hCountry = self.session.query((ShorturlOverview.short_url_requesCountry).label(
            'country'), func.count(ShorturlOverview.short_url_id).label('id')).filter(not_(ShorturlOverview.short_url_requesCountry == None)).filter(ShorturlOverview.short_url == ShortUrlInfo.short_code).filter(ShortUrlInfo.uuid == uu_id).group_by('country').order_by(desc('id')).all()
        # get total clicks by uuid
        tclicks = self.session.query(func.count(ShorturlOverview.short_url_id)).filter(
            ShorturlOverview.short_url == ShortUrlInfo.short_code).filter(ShortUrlInfo.uuid == uu_id).all()

        # get the day vistors
        dclick = self.session.query(ShorturlOverview).filter(
            and_(
                ShorturlOverview.short_url_id == uuid.id,
                ShorturlOverview.short_url_createTime >= self.getDay() + " 00:00:00",
                ShorturlOverview.short_url_createTime < self.getDay(
                    1) + " 00:00:00"
            )
        ).count()

        # print("~~~~~~~~~~~~~~hCountry")
        # print(hCountry)
        # print('~~~~~~~~~~~~~~~')
        # print(hIP)
        # print(accesslist)
        # print(hCountry)
        # print(tclicks)

        data['dclick'] = dclick
        data['tclicks'] = tclicks[0][0]
        # print(len(hCountry))
        # print(len(hIP))

        # get current day time
        daynow = datetime.datetime.now()
        daylist = self.getDay_list_7(daynow)

        dlist = []
        # get the 7 days list
        for d in daylist:
            dlist.append(d)
        list_week_day = dlist[::-1]
        num = [0, 0, 0, 0, 0, 0, 0, ]
        classes = list_week_day
        for j in range(len(classes)):
            for (d, n) in accesslist:
                if d[6:10] == classes[j]:
                    num[j] = n
                    break

        plt.title('Figue-1')
        plt.bar(classes, num)
        plt.xlabel('Last 7 days vistors')
        plt.ylabel("Number of clicks")
        plt.grid(True)
        #set y interval as 10
        y_major_locator=MultipleLocator(10)
        #get current x,y
        ax = plt.gca()
        ax.yaxis.set_major_locator(y_major_locator)
        plt.ylim(0,200)
        sio = BytesIO()
        plt.savefig(sio, format='png')
        plt.close()
        str1 = base64.encodebytes(sio.getvalue()).decode()
        src = 'data:image/png;base64,' + str(str1)
        data["src1"] = src




        day = datetime.datetime.now() - datetime.timedelta(days=7)
        daynow1 = datetime.datetime(day.year, day.month, day.day)
        daylist1 = self.getDay_list_7(daynow1)
        dlist1 = []
        for da in daylist1:
            dlist1.append(da)
        list_week_day1 = dlist1[::-1]
        num1 = [0, 0, 0, 0, 0, 0, 0, ]
        classes1 = list_week_day1
        for j in range(len(classes1)):
            for (d, n) in accesslist:
                if d[6:10] == classes1[j]:
                    num1[j] = n
                    break

        plt.title("Figue-2")
        plt.xlabel("Start from the past two weeks")
        plt.ylabel("Number of access")
        plt.plot(classes1, num1, color='red', linestyle='solid')
       
        y_major_locator = MultipleLocator(5)
        ax = plt.gca()
        ax.yaxis.set_major_locator(y_major_locator)
        plt.ylim(0,100)
        ax1=plt.subplot()
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        sio = BytesIO()
        plt.savefig(sio, format='png')
        plt.close()
        str1 = base64.encodebytes(sio.getvalue()).decode()
        src = 'data:image/png;base64,' + str(str1)
        data["src2"] = src
        data['uuid'] = uu_id
     
        if len(hCountry) and len(hIP) > 0:
            data['hCountry'] = hCountry[0][0]
            data['hIP'] = hIP[0][0]
            data['hIP1'] = hIP[0][0]
            data['hCountry1'] = hCountry[0][0]
            if len(hCountry) and len(hIP) > 1:
                print("pass~~~~~~~~~~~~~~")
                data['hCountry'] = hCountry[0][0]
                data['hIP'] = hIP[0][0]
                data['hIP1'] = hIP[0][0]
                data['hIP2'] = hIP[1][0]
                data['hCountry1'] = hCountry[0][0]
                data['hCountry2'] = hCountry[1][0]
                if len(hCountry) and len(hIP) > 2:
                    print("pass~~~~~~~~~~~~~~")
                    data['hCountry'] = hCountry[0][0]
                    data['hIP'] = hIP[0][0]
                    data['hIP1'] = hIP[0][0]
                    data['hIP2'] = hIP[1][0]
                    data['hIP3'] = hIP[2][0]
                    data['hCountry1'] = hCountry[0][0]
                    data['hCountry2'] = hCountry[1][0]
                    data['hCountry3'] = hCountry[2][0]
                    if len(hCountry) and len(hIP) > 3:
                        print("pass~~~~~~~~~~~~~~")
                        data['hCountry'] = hCountry[0][0]
                        data['hIP'] = hIP[0][0]
                        data['hIP1'] = hIP[0][0]
                        data['hIP2'] = hIP[1][0]
                        data['hIP3'] = hIP[2][0]
                        data['hIP4'] = hIP[3][0]
                        data['hCountry1'] = hCountry[0][0]
                        data['hCountry2'] = hCountry[1][0]
                        data['hCountry3'] = hCountry[2][0]
                        if len(hCountry) and len(hIP) > 4:
                            print("pass~~~~~~~~~~~~~~")
                            data['hCountry'] = hCountry[0][0]
                            data['hIP'] = hIP[0][0]
                            data['hIP1'] = hIP[0][0]
                            data['hIP2'] = hIP[1][0]
                            data['hIP3'] = hIP[2][0]
                            data['hIP4'] = hIP[3][0]
                            data['hIP5'] = hIP[4][0]
                            data['hCountry1'] = hCountry[0][0]
                            data['hCountry2'] = hCountry[1][0]
                            data['hCountry3'] = hCountry[2][0]
          
            self.render("staticurl.html", data=data)
        else:
            self.render("staticurl.html", data=data)

    def post(self):
        # status code 200:success 500:fail
        result = dict(statuscode=500)
        pageNumber = int(self.get_argument('pageNumber', 1))
        uuid = self.get_argument('uuid', None)
      
        try:
            dataNum = 10
            dataInfo = self.session.query(ShortUrlInfo, ShorturlOverview).filter(
                and_(
                    ShortUrlInfo.uuid == uuid,
                    ShorturlOverview.short_url_id == ShortUrlInfo.id
                )
            ).offset((pageNumber-1) * dataNum).limit(dataNum)
            
            # print("################datainfo")
            
            result['datainfo'] = []
            for r in dataInfo:
                obj = dict(
                    id = r.ShorturlOverview.short_url_id,
                    short_url_requestIP = r.ShorturlOverview.short_url_requestIP,
                    short_url_access_connectType = r.ShorturlOverview.short_url_access_connectType,
                    short_url_access_osType = r.ShorturlOverview.short_url_access_osType,
                    short_url_access_osName = r.ShorturlOverview.short_url_access_osName,
                    short_url_requestLocation = r.ShorturlOverview.short_url_requestLocation,
                    short_url_access_agent_name = r.ShorturlOverview.short_url_access_agent_name,
                    short_url_createTime = r.ShorturlOverview.short_url_createTime.strftime("%Y-%m-%d %H:%M:%S")
                )
                print('~~~~~~~~~~~~~~~~~~~~~d')
                print(obj)
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
