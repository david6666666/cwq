from bs4 import BeautifulSoup
import requests
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup = BeautifulSoup(demo, 'html.parser')
print(soup.title)
print(soup.a.string)
print(soup.a.attrs['class'])
'''
Tag                 标签，最基本的信息组织单元，分别用<>和</>标明幵头和结尾
Name                标签的名字，<p>…</p>的名字是'p'，格式：<tag>.name
Attributes          标签的属性，字典形式组织，格式：<tag>.attrs
NavigablcString     标签内非属性字符串，<>...</>中字符串，格式：<tag>.string  
Comment             标签内字符串的注释部分，一种特殊的Comment类型
'''