#测试继承的基本使用
# Python 支持多重继承，一个子类可以继承多个父类。继承的语法格式如下：
# class 子类类名(父类 1[，父类 2，...])：
# 类体
# 如果在类定义中没有指定父类，则默认父类是 object 类。也就是说，object 是所有类的父
# 类，里面定义了一些所有类共有的默认实现，比如：__new__()。
# 定义子类时，必须在其构造函数中调用父类的构造函数。调用格式如下：
# 父类名.__init__(self, 参数列表)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def say_age(self):
        print(self.name, "的年龄是：", self.__age)


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score

    # 构造函数中包含调用父类构
    #造函数。根据需要，不是必须。 子类并不会自动调用父类的__init__()，我
    #们必须显式的调用它。

print(Student.mro())

s = Student('cwq',25,100)
s.say_age()
print(s._Person__age)
print(dir(s))