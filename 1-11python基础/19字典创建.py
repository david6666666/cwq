"""
字典是”键值对“的无序可变序列，
    键是不可变数据，且不可重复。整数、浮点数、字符串、元组
    值是任意数据，且可重复
    创建：
        1.{}、dict()
        2.zip()
        3.通过fromkeys创建值为空的字典
"""
a = {'name':'cwq', 'age':18, 'job':'programmer'}
print(a.get('name'))

b = dict(name='cwq', age=18, job='programmer')
print(b)

k = ['name', 'age', 'job']
v = ['cwq', 19, 'programmer']
s = dict(zip(k,v))
print(s)

c = dict.fromkeys(['name', 'age', 'job'])
print(c)