#修改原列表，不建新列表的排序
a = [20, 10, 30, 40]
print(id(a))
a.sort()
print(a)

a = [10, 20, 30, 40]
a.sort(reverse=True)
print(a)
print("--------------------")
#随机排序
import random
random.shuffle(a)
print(a)

#建新列表的排序    用内置函数sorted()
print("--------------------")
a = [20, 10, 30, 40]
a = sorted(a)
print(a)

#reversed()返回迭代器
print("--------------------")
a = [20, 10, 30, 40]
c = reversed(sorted(a))
print(c)
print(list(c))

#最大值max()   最小值min()    求和sum()
print("--------------------")