#集合的底层是字典实现，集合的所有元素都是字典中的“键对象”，因此是不能重复
#的且唯一的

a = {30, 50, 70}
print(a)
a.add(90)
print(a)

#使用set()函数

b = [20, 10, 30, 40]
c = set(b)
print(c)
'''
a|b    并集
a&b     交集
'''