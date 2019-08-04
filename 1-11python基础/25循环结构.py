'''
    for 变量 in (20,30,40):
        循环体语句
'''

for x in (10,20,30):
    print(x*30,end=' ')
print()
for x in "abcdef":
    print(x,end=' ')
print()
a = {'name':'cwq', 'age':18, 'job':'programmer'}
for x in a.items():
    print(x,end=' ')
print()
for x in range(0,10,2):
    print(x,end=' ')
print()
for x in range(5):
    for y in range(5):
        print(x,end='\t')
    print()
print()

for x in range(1,10):
    for y in range(1,x+1):
        print("{0}*{1}={2}".format(x,y,(x*y)),end='\t')
    print()

#break 语句       结束整个循环，用于最近的一层循环
#continue 语句    结束本次循环，继续下一次。用于最近的一层循环
#else语句     如果for、while语句没有被break语句结束，
#               则会执行else子句，否则不执行
