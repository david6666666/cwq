# Python 支持多继承，如果父类中有相同名字的方法，在子类没有指定父类名时，解释器将
# “从左向右”按顺序搜索。
#多重继承
class A:
    def aa(self):
        print("aa")
    def say(self):
        print("say AAA!")
class B:
    def bb(self):
        print("bb")
    def say(self):
        print("say BBB!")
class C(B,A):
    def cc(self):
        print("cc")
c = C()
print(C.mro()) #打印类的层次结构
c.say() #解释器寻找方法是“从左到右”的方式寻找，此时会执行 B
#类中的 say()