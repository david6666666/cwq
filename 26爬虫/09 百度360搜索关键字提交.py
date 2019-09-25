'''
搜索引擎关键词提交接口
百度的关键词接□:
http://www.baidu.com/s?wd=keyword
360的关键词接□:
http ://www.so.com/s?q=keyword
'''
import requests
kv = {'wd':'python'}
try:
    r = requests.get('http://www.baidu.com/s?wd=keyword',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')