class Student:
    def __init__(self,name,score): #构造方法第一个参数必须为 self
        self.name = name #实例属性
        self.score = score
    def say_score(self): #实例方法
        print(self.name,'的分数是：',self.score)

s1 = Student('张三',80) #s1 是实例对象，自动调用__init__()方法
s1.say_score()