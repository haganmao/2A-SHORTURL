from view.core import coreHandler
from pyecharts import options as opts
from pyecharts.charts import Pie
from model.database import ShortUrlInfo, ShorturlOverview
from sqlalchemy import and_, join, func, desc

class pieHandler(coreHandler):
    def get(self):
        

        uuid = self.get_argument('uuid',None)
        print("~~~~~~~~~~~~~~~~uuid")
        print(uuid)

        
        deviceinfo = self.session.query(ShorturlOverview.short_url_access_connectType.label('device'),func.count(ShorturlOverview.short_url_id)).filter(ShortUrlInfo.uuid == uuid).filter(ShortUrlInfo.short_code==ShorturlOverview.short_url).group_by('device').all()

        osinfo = self.session.query(ShorturlOverview.short_url_access_osType.label('osinfo'),func.count(ShorturlOverview.short_url_id)).filter(ShortUrlInfo.uuid == uuid).filter(ShortUrlInfo.short_code == ShorturlOverview.short_url).group_by('osinfo').all()

        # print("~~~~~~~~~~~deviceinfo")
        # print(deviceinfo)
      
        inner_data_pair = []        
        for device_data in deviceinfo:
            dinfolist_item = []
            dinfolist_item.append(device_data[0])
            dinfolist_item.append(device_data[1])
            inner_data_pair.append(dinfolist_item)

        outer_data_pair = []
        for os_data in osinfo:
            os_data_item = []
            os_data_item.append(os_data[0])
            os_data_item.append(os_data[1])
            outer_data_pair.append(os_data_item)
        
        # print("~~~~~~~~~~~inneinner_data")
        # print(inner_data_pair)
        # print("~~~~~~~~~~~~~osinfo")
        # print(outer_data_pair)
        

        pie = (Pie(init_opts=opts.InitOpts(width="800pX", height="400px"))
                .add(
                    series_name="Device From",
                    data_pair=inner_data_pair,
                    radius=[0, "30%"],
                    label_opts=opts.LabelOpts(position="inner"),
                )
                .add(
                    series_name="OS Type From",
                    radius=["40%", "55%"],
                    data_pair=outer_data_pair,
                    label_opts=opts.LabelOpts(
                        position="outside",
                        formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                        background_color="#eee",
                        border_color="#aaa",
                        border_width=1,
                        border_radius=4,
                        rich={
                            "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                            "abg": {
                                "backgroundColor": "#e3e3e3",
                                "width": "100%",
                                "align": "right",
                                "height": 22,
                                "borderRadius": [4, 4, 0, 0],
                            },
                            "hr": {
                                "borderColor": "#aaa",
                                "width": "100%",
                                "borderWidth": 0.5,
                                "height": 0,
                            },
                            "b": {"fontSize": 16, "lineHeight": 33},
                            "per": {
                                "color": "#eee",
                                "backgroundColor": "#334455",
                                "padding": [2, 4],
                                "borderRadius": 2,
                            },
                        },
                    ),
                )
                .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"),
                title_opts=opts.TitleOpts(title="Link Access Device Statistics",pos_right="center"))
                .set_series_opts(
                    tooltip_opts=opts.TooltipOpts(
                        trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
                    )
                ))
        pie.render("./template/pie.html")
        self.render('pie.html')
