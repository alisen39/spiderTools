import re
'''
说明：
    
'''
def re_cookie(cookieStr):
    print(cookieStr.encode('utf-8'))
    key = re.findall('[\t|\n]([\w*|\.]*)=',cookieStr)
    val = re.findall('=[\n\t]*(.*)\n',cookieStr)
    cookies = {}
    for i in range(0, len(key)):
        cookies[key[i]] = val[i]
        print(key[i], val[i])
    print(key)
    print(len(key))
    print(len(val))
    print(cookies)

a ='''
	_lxsdk_cuid=161f5f5dd10c8-0a66fbd1e4c7488-4c322172-100200-161f5f5dd10d
	__mta=41660957.1520249987479.1529677385511.1529677390548.8
	_hc.v=38ad1a4c-5533-7aaf-6a5d-b599bfc125ff.1522035276
	wm_order_channel=default
	openh5_uuid=38ad1a4c-5533-7aaf-6a5d-b599bfc125ff
	terminal=i
	openh5_uuid=38ad1a4c-5533-7aaf-6a5d-b599bfc125ff
	w_latlng=0,0
	w_actual_lat=23135075
	w_actual_lng=113357076
	w_uuid=RnKYIBB-jWY3thKIqde6rbMRnU4NbquSqfrjvWBYjKI8VK-M8S1uBvScQ2Ohg0Wr
	JSESSIONID=z56ndicns7t419dluh1w2r75f
	w_visitid=d723370a-acc2-457d-999c-c2c5b7c5a1c6


'''
re_cookie(a)