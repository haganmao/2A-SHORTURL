
from view.core import coreHandler
from pyecharts.charts import Bar, Pie, Calendar, Map
from pyecharts import options as opts


# staticurl handler
class staticurlHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle="See the world with Statistic url"
        )


        # get headers info exp client devece info,broswer
        header = self.request.headers
        # if exists
        if header:
            print("#######################")
            print(header)

        else:
            print('no header info')


    
        self.render("staticurl.html", data=data)
        
