"""
    增加
        append()
        +
        entend()
        insert()
        *
    删除
        del     删除指定位置元素
        pop()   删除某个元素并且返回
        remove()    删除首次出现的指定元素， 若不存在该元素则跑出异常
"""

a = [20, 40]
a.append(100)
print(a)
a = a + [200]
print(a)
a.extend([300, 400])
print(a)
a.insert(2,90)
print(a)
print("--------------------")

b = [100, 200, 888, 300, 400]
del(b[2])
print(b)
bp = b.pop(2)
print(bp, b)
b.remove(100)
print(b)