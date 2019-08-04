"""
    2.update()
    3.删除 del() clear() pop()
    4.popitem()随机删除和返回该键值对
"""
a = {'name':'cwq', 'age':18, 'job':'programmer'}
b = {'name':'cwqcwq', 'money':666666, 'sex':'man'}
a['address'] = 'sdu'
print(a)
a.update(b)
print(a)

c = b.pop('name')
print(c)