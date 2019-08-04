# """
# 列表：
#
# names = ['a','b','c','d']
# 1、追加：names.append()
#
# >>> names.append('e')
# >>> names
# ['a', 'b', 'c', 'd', 'e']
# 2、删除：pop，remove，del
#
# 1）pop()
#
# >>> names.pop()
# 'e'
# 如果没有指定下标，则默认会删除最后一个元素
#
# >>> names.pop(2)
# 'c'
# 指定下标时，就会删除下标所对应的元素
#
# 2）remove()
#
# >>> names.remove('e')
# >>> names
# ['a', 'b', 'c', 'd']
# 3）del
#
# >>> del names[4]
# >>> names
# ['a', 'b', 'c', 'd']
# 3、查找元素所在位置：index()
#
# >>> names.index('c')
# 2
# 4、统计元素的次数：count()
#
# >>> names.append('d')
# >>> names.count('d')
# 2
# 5、反转：reverse()
#
# >>> names.reverse()
# >>> names
# ['d', 'c', 'b', 'a']
# 6、清空：clear()
#
# >>> names.clear()
# >>> names
# []
# 7、插入：insert()
#
# >>> names.insert(2,'devilf')
# >>> names
# ['a', 'b', 'devilf', 'c', 'd']
# 还有其他的插入方法：
#
# >>> names[3] = 'lebron'
# >>> names
# ['a', 'b', 'devilf', 'lebron', 'd']
# 8、排序：sort()按照ascii码来进行排序
#
# >>> names.insert(4,'&&')
# >>> names
# ['a', 'b', 'd', 'devilf', '&&', 'lebron']
# >>> names.sort()
# >>> names
# ['&&', 'a', 'b', 'd', 'devilf', 'lebron']
# 9、拼接两个列表：extend()
#
# >>> names.extend(place)
# >>> names
# ['&&', 'a', 'b', 'd', 'devilf', 'lebron', 'beijing', 'shandong', 'usa']
# 10、对列表进行切片处理
#
# 1）列出所有的元素
#
# >>> names[::]
# ['&&', 'a', 'b', 'd', 'devilf', 'lebron', 'beijing', 'shandong', 'usa']
# 2）列出最后一个元素，从中间位置开始，列出后面所有的元素
#
# >>> names[-1]
# 'usa'
# >>> a = int(len(names)/2)
# >>> names[a:]
# ['devilf', 'lebron', 'beijing', 'shandong', 'usa']
# 11、复制：copy()
#
# >>> names.copy()
# ['&&', 'a', 'b', 'd', 'devilf', 'lebron', 'beijing', 'shandong', 'usa']
#  另外的几种复制的方法：
#
# >>> info = ['name',['a',100]]
# >>> n1 = copy.copy(info)
# >>> n2 = info[:]
# >>> n3 = list(info)
# 在使用copy.copy()时，需要导入copy模块
#
# 这些均是浅copy
#
# 例如：
#
# 复制代码
# >>> info
# ['name', ['a', 100]]
# >>> n1 = info[:]
# >>> n2 = copy.copy(info)
# >>> n1
# ['name', ['a', 100]]
# >>> n1[0] = 'devilf'
# >>> n2[0] = 'lebron'
# >>> n1;n2
# ['devilf', ['a', 100]]
# ['lebron', ['a', 100]]
# >>> n1[1][1] = 80
# >>> n1
# ['devilf', ['a', 80]]
# >>> n2
# ['lebron', ['a', 80]]
# 复制代码
# 这里可以看到修改n1列表中的值，n2中的值也会跟着改变，这就是浅copy,也就是说，浅copy会复制原列表的内存地址，也就是说，我们修改了n1和n2，就是修改了指向同一内存地址的对象，所以info列表会变化，n1和n2都会变化，例如：
#
# >>> info
# ['name', ['a', 80]]
# """

a = [x*2 for x in range(100) if x%9==0]
print(a)