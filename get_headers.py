import re

h1 = '''
Host: i.waimai.meituan.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0
Accept: application/json
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Referer: http://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId=544259269263747&source=shoplist&initialLat=&initialLng=&actualLat=23.135075&actualLng=113.357076
Content-Type: application/x-www-form-urlencoded
Origin: http://h5.waimai.meituan.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

'''

print(h1.encode('utf-8'))
key = re.findall('[\t|\n]([\w*|\.|-]*):',h1)
val = re.findall(':[\n\t]*(.*)\n',h1)
header = {}
print(key)
print(val)
for i in range(0,len(key)):
    header[key[i]] = val[i].lstrip(' ')
    print(key[i],val[i])

print(len(key))
print(len(val))
print(header)

