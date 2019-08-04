# 1. 成员继承：子类继承了父类除构造方法之外的所有成员。
# 2. 方法重写：子类可以重新定义父类中的方法，这样就会覆盖父类的方法，也称为“重写”

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_age(self):
        print(self.name,"的年龄是：",self.age)
    def say_name(self):
        print("我是",self.name)

class Student(Person):
    def __init__(self,name,age,score):
        self.score = score
        Person.__init__(self,name,age) #构造函数中包含调用父类构造函数
    def say_score(self):
        print(self.name,"的分数是：",self.score)
    def say_name(self): #重写父类的方法
        print("报告老师，我是",self.name)

s1 = Student("张三",15,85)
s1.say_score()
s1.say_name()
s1.say_age()