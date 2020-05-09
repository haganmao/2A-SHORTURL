import os
from config import settings
from ip2Region.ip2Regionpy import Ip2Region

# get ip location, ip2Region library
def getIpLocation(ip):
    ip_region_DB_path = settings['ip2Region_DB_path']
    ip2region = Ip2Region(ip_region_DB_path)
    iplocation = ip2region.memorySearch(ip)
    return iplocation
