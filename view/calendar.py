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
        data = []
        for d in accesslist:
            clist_item = []
            clist_item.append(d[0])
            clist_item.append(d[1])
            data.append(clist_item)
 
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
                max_=200,
                min_=1,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )

   
        calendar.render(path=settings['template_path'] + '/calendar.html', encoding='utf-8')
        self.render('calendar.html')
