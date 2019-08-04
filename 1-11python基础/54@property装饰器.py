'''
@property 可以将一个方法的调用方式变成“属性调用”。下面是一个简单的示例，让大
家体会一下这种转变：
'''
#
# #简单测试@property
# class Employee:
#
#     @property
#     def salary(self):
#         return 30000;
#
# emp1 = Employee()
# print(emp1.salary) #打印 30000
# print(type(emp1.salary)) #打印<class 'int'>
#
# #emp1.salary() #报错：TypeError: 'int' object is not
# callable
# #emp1.salary =1000          #@property 修饰的属性，如果没有
# #加 setter 方法，则为只读属性。此处修改报错：AttributeError: can't set
# #attribute


#测试@property
class Employee:
    def __init__(self, name, salary):
        self.name = name

        self.__salary = salary

    @property  # 相当于 salary 属性的 getter 方法
    def salary(self):
        print("月薪为{0},年薪为{1}".format(self.__salary,(12*self.__salary)))

        return self.__salary

    @salary.setter
    def salary(self, salary):  # 相当于 salary 属性的 setter 方法
        if (0 < salary < 1000000):
            self.__salary = salary

        else:
             print("薪水录入错误！只能在 0-1000000 之间")
emp1 = Employee("高淇", 100)
print(emp1.salary)
emp1.salary = -200