import datetime
import random

from view.core import coreHandler
from pyecharts.charts import Calendar
from pyecharts import options as opt
from model.database import ShortUrlInfo, ShorturlOverview
from sqlalchemy import and_, join, func, desc
from config import settings


class calendarHandler(coreHandler):
    def get(self):
        begin = datetime.date(2020, 1, 1)
        end = datetime.date(2020, 12, 31)

        uu_id = self.get_argument('uuid', None)

        accesslist = self.session.query(func.date_format(ShorturlOverview.short_url_createTime, '%Y-%m-%d').label(
            'date'), func.count(ShorturlOverview.short_url_id)).filter(ShorturlOverview.short_url == ShortUrlInfo.short_code).filter(ShortUrlInfo.uuid == uu_id).group_by('date').order_by('date').all()
        # print(accesslist)

        data = []
        for d in accesslist:
            clist_item = []
            clist_item.append(d[0])
            clist_item.append(d[1])
            data.append(clist_item)
        # print('~~~~~~~~~~~~~~~~~~~~clist')
        # print(data)
        
        # data = [
        #     [str(begin + datetime.timedelta(days=i)),
        #      random.randint(50, 200)]
        #     for i in range((end - begin).days + 1)
        # ]
        # data = [['2020-01-02', 196], ['2020-01-04', 140], ['2020-01-05', 173], ['2020-01-06', 61], ['2020-01-07', 78], ['2020-01-08', 183], ['2020-01-09', 103], ['2020-01-10', 50]]
        # print('~~~~~~~~~~~~data')
        # print((data))
     
        calendar = Calendar()
        calendar.add('', data,
                     calendar_opts=opt.CalendarOpts(
                         range_='2020',
                         daylabel_opts=opt.CalendarDayLabelOpts(name_map='en'),
                         monthlabel_opts=opt.CalendarMonthLabelOpts(
                             name_map='en'),
                     ),
                     )

        calendar.set_global_opts(
            title_opts=opt.TitleOpts(
                title='Calendar - The number of clicks per day in 2020'),
            visualmap_opts=opt.VisualMapOpts(
                max_=400,
                min_=1,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )

        # calendar.render(path='./template/calendar.html')
        # path = settings['template_path']
        calendar.render(path=settings['template_path'] + '/calendar.html', encoding='utf-8')
        # print('~~~~~~~~~~~~~~~~~~path')
        # print(path)
        self.render('calendar.html')
