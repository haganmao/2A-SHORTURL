import os 
from tool.ip2Region import Ip2Region
import config
import geoip2
from geoip2 import database

def ip2Location(ip):
    ipdb_path = config.settings['ip2Region_DB_path']
     
    # os.path.join(
    #     os.path.dirname(
    #         os.path.dirname(
    #             __file__
    #         )
    #     ), "static\ip2region-master\data\ip2region.db"
    # )
    
    i2R = Ip2Region(ipdb_path)
    ip2location = i2R.memorySearch(ip)
    return ip2location



