import geoip2
from geoip2 import database
import os



geoip2_db = os.path.join(
        os.path.dirname(
            os.path.dirname(
                __file__
            )
        ), "static\GeoLite2-City_20200512\GeoLite2-City.mmdb"
    )


def getAddr(ip):
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


# ip = '2407:7000:9ba3:b200:933:e416:1e8b:91e4'
# def findValidIPinfo():
#     result_locationinfo = getAddr(ip)
#     result_locationCountry =  result_locationinfo['response_contury']
#     result_locationsuburb=  result_locationinfo['response_suburb']
#     result_locationcity =  result_locationinfo['response_city']
#     result_locationcontinent =  result_locationinfo['response_continent']
   
#     assert result_locationCountry == 'New Zealand'
#     assert result_locationcity == 'Wellington'
#     assert result_locationsuburb == 'Lower Hutt'
#     assert result_locationcontinent == 'Oceania'
#     assert result_locationinfo['find'] == True
# findValidIPinfo()

ip = '127.0.0.1'
def findInValidIPinfo():
    result_locationinfo = getAddr(ip)
    assert result_locationinfo['addr'] == 'Location Not Aviliable This Ip Address'
    assert result_locationinfo['find'] == True

findInValidIPinfo()
