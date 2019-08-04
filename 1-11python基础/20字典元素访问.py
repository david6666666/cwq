"""
字典元素的访问:
    1.通过[键]获得”值“。若键不存在则抛出异常
    2.通过get()方法获得”值”，若不存在返回None或者自己设定
    3.列出所有键值对 items()
    4.列出所有的键keys(),列出所有的值values()
    5.len() 键值对个数
    6.检测一个“键”是否在字典中
"""
a = {'name':'cwq', 'age':18, 'job':'programmer'}
print(a['name'])
print(a.get('job'))
print(a.items())
print(a.keys())
print(a.values())
print('name' in a)