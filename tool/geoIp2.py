import geoip2
import config
from geoip2 import database


def getAddr(ip):
    geoip2_db = config.settings['geoip2_DB_path']
    reader = geoip2.database.Reader(geoip2_db)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3")        
    locationDetail = dict()

    try:
        response = reader.city(ip)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2")
        locationDetail["response_suburb"] = response.city.names['en']
        locationDetail["response_city"] = response.subdivisions.most_specific.names['en']
        locationDetail["response_contury"] = response.country.names['en']
        locationDetail["response_continent"] = response.continent.names['en']
        locationDetail["addr"] = locationDetail["response_suburb"] + ', ' + locationDetail["response_city"] + \
            ', ' + locationDetail["response_contury"] + ', ' + locationDetail["response_continent"]
        # addr.format()
        locationDetail['find'] = 1
        return locationDetail
    except Exception as exception:
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        locationDetail['find'] = 0
        locationDetail["addr"] = 'Location Not Aviliable This Ip Address'
        return locationDetail
    # print("###########")
    # print(addr)
