
import re
def re_data(data):
    key_rule='(.*)\t'
    key = re.findall(key_rule,data)
    value_rule = '\t(.*)'
    value = re.findall(value_rule,data)

    print(len(key))
    print(len(value))
    result = {}
    if len(key) == len(value):
        for i in range(len(key)):
            result[key[i]] = value[i]
    print(result)



if __name__ == '__main__':
    a = '''
_token	
address	
channel	6
cityId	
gpsLat	23.135075
gpsLng	113.357076
lat	23.135075
lng	113.357076
mtWmPoiId	544259269263747
orderPlatform	
shopId	0
source	shoplist
wm_actual_latitude	23135075
wm_actual_longitude	113357076
wm_latitude	0
wm_longitude	0
    '''
    re_data(a)