'''
lambda 表达式可以用来声明匿名函数。lambda 函数是一种简单的、在同一行中定义函数
的方法。lambda 函数实际生成了一个函数对象。
lambda 表达式只允许包含一个表达式，不能包含复杂语句，该表达式的计算结果就是函数
的返回值。

lambda 表达式的基本语法如下：
        lambda arg1,arg2,arg3... : <表达式>
arg1/arg2/arg3 为函数的参数。<表达式>相当于函数体。运算结果是：表达式的运算结果。
'''

f = lambda a,b,c:a+b+c
print(f)
print(f(2,3,4))

g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]
print(g[0](6),g[1](7),g[2](8))