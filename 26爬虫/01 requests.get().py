'''
Response对象的属性
r.status_code   HTTP请求的返回状态，200表示连接成功，404表示失败
r.text          HTTP响应内容的字符串形式，即，url对应的页面内容
r.encoding      从HTTP header中猜测的响应内容编码方式 encoding
r.apparent      从内容中分析出的响应内容编码方式（备选编码方式）
r.content       HTTP响应内容的二进制形式
'''
import requests
r =  requests.get('http://www.baidu.com')
print(r.status_code)
print(type(r))
print(r.headers)
