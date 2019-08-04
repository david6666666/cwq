#测试eval()函数
'''
功能：将字符串 str 当成有效的表达式来求值并返回计算结果。
语法： eval(source[, globals[, locals]]) -> value
参数：
source：一个 Python 表达式或函数 compile()返回的代码对象
globals：可选。必须是 dictionary
locals：可选。任意映射对象

eval 函数会将字符串当做语句来执行，因此会被注入安全隐患。比如：字符串中含有删除文
件的语句。那就麻烦大了。因此，使用时候，要慎重！！！
'''

s ="print('abcde')"
eval(s)

a = 10
b = 20
c = eval("a+b")
print(c)

dict1 = dict(a=100,b=200)
d = eval("a+b",dict1)
print(d)