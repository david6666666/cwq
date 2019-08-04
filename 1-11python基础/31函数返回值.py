def my_avg(a,b):
    return (a+b)/2

c = my_avg(10,20)
print(c)


#测试函数也是对象

def test01():
    print('sxtsxt')

test01()
c = test01
c()
print(id(test01))
print(id(c))