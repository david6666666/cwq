'''
为了更深入的了解参数传递的底层原理，我们需要讲解一下“浅拷贝和深拷贝”。我们可以
使用内置函数：copy(浅拷贝)、deepcopy(深拷贝)。

浅拷贝：不拷贝子对象的内容，只是拷贝子对象的引用。
深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象

传递不可变对象是浅拷贝
'''

#测试浅拷贝、深拷贝

import copy
def testCopy():
    '''测试浅拷贝'''
    a= [10,20,[5,6]]
    b = copy.copy(a)

    print('a:',a)
    print('b:',b)

    b.append(30)
    b[2].append(7)

    print('浅拷贝......')
    print('a:',a)
    print('b:',b)

def testDeepCopy():
    '''测试深拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)
    print("a", a)
    print("b", b)
    b.append(30)
    b[2].append(7)
    print("深拷贝......")
    print("a", a)
    print("b", b)
testCopy()
print("*************")
testDeepCopy()