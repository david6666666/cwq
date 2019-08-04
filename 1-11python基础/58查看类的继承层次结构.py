class A:pass
class B(A):pass
class C(B):pass
print(C.mro())

#dir()查看对象属性

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name, "的年龄是：", self.age)

obj = object()
print(dir(obj))
s2 = Person("高淇", 18)
print(dir(s2))