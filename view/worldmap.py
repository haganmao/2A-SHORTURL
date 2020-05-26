from view.core import coreHandler
from pyecharts import options as opts
from pyecharts.charts import Map
from sqlalchemy import and_, join, func
from model.database import ShortUrlInfo, ShorturlOverview
from view.staticurl import staticurlHandler


class worldmapHandler(staticurlHandler):
    def get(self):

        uuid = self.get_argument('uuid', None)
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print(uuid)

        countrylist = self.session.query(func.count(ShorturlOverview.short_url), ShorturlOverview.short_url_requesCountry.label(
            'country')).filter(ShorturlOverview.short_url == ShortUrlInfo.short_code).filter(ShortUrlInfo.uuid == uuid).group_by('country').all()
        print('~~~~~~~~~~~~~~~~~~~~~~countrylist')
        print(countrylist)

        
        clist = ['Singapore Rep.', 'Dominican Rep.', 'Palestine', 'Bahamas', 'Timor-Leste', 'Afghanistan', 'Guinea-Bissau', "Côte d'Ivoire", 'Siachen Glacier', 'Br. Indian Ocean Ter.', 'Angola', 'Albania', 'United Arab Emirates', 'Argentina', 'Armenia', 'French Southern and Antarctic Lands', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'The Bahamas', 'Bosnia and Herz.', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Brunei', 'Bhutan', 'Botswana', 'Central African Rep.', 'Canada', 'Switzerland', 'Chile', 'China', 'Ivory Coast', 'Cameroon', 'Dem. Rep. Congo', 'Congo', 'Colombia', 'Costa Rica', 'Cuba', 'N. Cyprus', 'Cyprus', 'Czech Rep.', 'Germany', 'Djibouti', 'Denmark', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands', 'France', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Guinea', 'Gambia', 'Guinea Bissau', 'Eq. Guinea', 'Greece', 'Greenland', 'Guatemala', 'French Guiana', 'Guyana', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'India', 'Ireland', 'Iran', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Korea', 'Kosovo', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Morocco', 'Moldova', 'Madagascar', 'Mexico', 'Macedonia', 'Mali', 'Myanmar', 'Montenegro', 'Mongolia', 'Mozambique', 'Mauritania', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Papua New Guinea', 'Poland', 'Puerto Rico', 'Dem. Rep. Korea', 'Portugal', 'Paraguay', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'W. Sahara', 'Saudi Arabia', 'Sudan', 'S. Sudan', 'Senegal', 'Solomon Is.', 'Sierra Leone', 'El Salvador', 'Somaliland', 'Somalia', 'Serbia', 'Suriname', 'Slovakia', 'Slovenia', 'Sweden', 'Swaziland', 'Syria', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'East Timor', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Vanuatu', 'West Bank', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe', 'Comoros']
        value = []
        attr = []

        for k in countrylist:
            for c in clist:
                if c == k[1]:
                    value.append(k[0])
                    attr.append(k[1])
                    break
        print("~~~~~~~~~~~~~~~~~")
        print(value)
        print(attr)
        

        map = Map()
        map.add('Total Clicked', [list(z) for z in zip(attr, value)], 'world')
        map.set_series_opts(label_opts=opts.LabelOpts(is_show=False),init_opts=opts.InitOpts(width="650px", height="500px"))
        map.set_global_opts(
            title_opts=opts.TitleOpts(title="Link Access World Map Distribution"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
        )
        map.render(path="./template/worldmap.html")
        self.render('worldmap.html')
