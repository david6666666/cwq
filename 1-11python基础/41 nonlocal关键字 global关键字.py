'''
nonlocal 用来声明外层的局部变量。
global 用来声明全局变量。
'''

a = 100
def outer():
    b = 10
    def inner():
        nonlocal b #声明外部函数的局部变量
        print("inner b:",b)
        b = 20
        global a #声明全局变量
        a = 1000
    inner()
    print("outer b:",b)
outer()
print("a：",a)