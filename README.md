## 说明
* 此工具类主要为了解决使用fiddler进行抓包时将header，data，cookie快速转换为python的字典的方法。

* 需在python3下使用

## 使用方法
以get_data.py举例:

> 1. 将WebForms下的值复制出来
![cebbdede30b4f036fe2e0883d2b62890](./img/2145B365-CF61-4801-B4C0-CA69FB348329.png)
> 2. 运行后的结果为：![37a980532a9bba13adba03487a22d200](./img/1B05DB95-7FF0-4527-A30D-6510A0E43FD1.png)

> 最后一行的值便是python的字典格式，也是requests,scrapy支持的data格式。

## 注意
* get_headers.py 仅支持解析从`Raw`里复制出来的值
* get_data.py 仅支持解析从`WebForms`里复制出来的值
* get_cookie.py 仅支持解析从`Cookies`里复制出来的值
