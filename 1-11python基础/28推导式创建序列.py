'''
    列表推导式：
        [表达式 for item in 可迭代对象 if 条件判断]
    字典推导式：
        {key_expression: value_expression for 表达式 in 可迭代对象}
    集合推导式：
        {表达式    for 表达式 in 可迭代对象}
    生成器推导式：
        一个生成器只能运行一次
'''
a = [x*2 for x in range(2,10) if x%2==0]
print(a)

cells = [(row,col) for row in range(1,10) for col in range(1,10)]
print(cells)

#统计文本中字符出现的次数
mytxt = 'i love you,i love cr,i love dota2'
char_count = {x:mytxt.count(x) for x in mytxt}
print(char_count)

b = {x for x in range(100) if x%6==0}
print(sorted(b,reverse=True))