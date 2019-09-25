'''
标签树的下行遍历
.contents	子节点的列表，将 <tag>所有儿子节点存人列表
.children	子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
.descendants子孙节点的迭代类型，包含所有子孙节点，用于循环遍历

标签树的上行遍历
.parent     节点的父亲标签
.parents    节点先辈标签的迭代类型，用于循环遍历先辈节点
标签树的平行遍历
.next_sibling       返回按照HTML文本顺序的下一个平行节点标签
.previou$_sibling   返回按照HTML文本顺序的上一个平行节点标签
•next_siblings      迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
.preVi〇US_Sibliiigs迭代类型，返回按照HTML文本顺序的前续所有平行节点标签
'''
from bs4 import BeautifulSoup
import requests
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup = BeautifulSoup(demo, 'html.parser')
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)