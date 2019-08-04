'''
实例属性是从属于实例对象的属性，也称为“实例变量”。他的使用有如下几个要点：
    1. 实例属性一般在__init__()方法中通过如下代码定义：
        self.实例属性名 = 初始值
    2. 在本类的其他实例方法中，也是通过 self 进行访问：
        self.实例属性名
    3. 创建实例对象后，通过实例对象访问：
        obj01 = 类名() #创建对象，调用__init__()初始化属性
        obj01.实例属性名 = 值 #可以给已有属性赋值，也可以新加属性

实例方法是从属于实例对象的方法。实例方法的定义格式如下：
    def 方法名(self [, 形参列表])：
        函数体
    方法的调用格式如下：
        对象.方法名([实参列表])
要点：
1. 定义实例方法时，第一个参数必须为 self。和前面一样，self 指当前的实例对象。
2. 调用实例方法时，不需要也不能给 self 传参。self 由解释器自动传参。

    其他操作：
        1. dir(obj)可以获得对象的所有属性、方法
        2. obj.__dict__ 对象的属性字典
        3. pass 空语句
        4. isinstance（对象,类型） 判断“对象”是不是“指定类型”
'''

class Student:
    def __init__(self,name,score): #构造方法第一个参数必须为 self
        self.name = name #实例属性
        self.score = score
    def say_score(self): #实例方法
        print(self.name,'的分数是：',self.score)

s1 = Student('张三',80) #s1 是实例对象，自动调用__init__()方法
s1.say_score()
#Student.say_score(s1)


s1.age = 32
s1.salary = 3000
print(s1.salary)
print(dir(s1))
print(s1.__dict__)
print(isinstance(s1,Student))