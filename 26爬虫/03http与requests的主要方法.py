'''
requests.request()          构造一个请求，支撑以下各方法的基础方法
requests.get()              获取HTML网页的主要方法，对应于HTTP的GET
requests.head()             获取HTML网页头信息的方法，对应于HTTP的HEAD
requests.post()             向HTML网页提交POST请求的方法，对应于HTTP的POST
requests.put()              向HTML网页提交PUT请求的方法，对应于HTTP的PUT
requests.patch()            向HTML网页提交局部修改请求，对应于HTTP的PATCH
requests.delete()           向HTML页面提交删除请求，对应于HTTP的DELETE

HTTP协议对资源的操作
GET     请求获取URL位置的资源
HEAD	请求获取URL位H资源的响应消息报告，即获得该资源的头部信息
--------------------------------------------------------
POST	请求向URL位置的资源后附加新的数据
PUT	    请求向URL位置存储一个资源，覆盖原URL位置的资源
PATCH	请求局部更新URL位置的资源，即改变该处资源的部分内容
DELETE  请求删除URL位置存储的资源
'''