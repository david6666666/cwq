'''
    Python 在查找“名称”时，是按照 LEGB 规则查找的：
        Local-->Enclosed-->Global-->Built in
    Local 指的就是函数或者类的方法内部
    Enclosed 指的是嵌套函数（一个函数包裹另一个函数，闭包）
    Global 指的是模块中的全局变量
    Built in 指的是 Python 为自己保留的特殊名称。
如果某个 name 映射在局部(local)命名空间中没有找到，接下来就会在闭包作用域
(enclosed)进行搜索，如果闭包作用域也没有找到，Python 就会到全局(global)命名空
间中进行查找，最后会在内建(built-in)命名空间搜索 （如果一个名称在所有命名空间
中都没有找到，就会产生一个 NameError）。
'''

#测试 LEGB
str = "global"
def outer():
    str = "outer"
    def inner():
        str = "inner"
        print(str)
    inner()
outer()