
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
shopId	0
source	shoplist
    '''
    re_data(a)
