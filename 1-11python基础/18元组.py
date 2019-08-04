'''
元组属于不可变序列
    没有增、改、删等操作
    创建：
        1.(,)带逗号
        2.tuple()


'''
a = (20, 10, 30, 9)
a = sorted(a)           #sorted()返回的还是列表
print(a)
print("--------------------")
#zip（列表1，列表2，。。。。）将多个列表对应位置的元素组合成元组，并返回zip对象
a = [10,20,30]
b = [40,50,60]
c = [70,80,90]
d = zip(a,b,c)
print(d)
print(list(d))
print("--------------------")
#生成器
s = (x*2 for x in range(5))
# print(tuple(s))
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
