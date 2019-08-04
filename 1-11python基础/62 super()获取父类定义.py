#super()
class A:
    def say(self):
        print("A: ",self)
        print("say AAA")
class B(A):
    def say(self):
        #A.say(self) 调用父类的 say 方法
        super().say() #通过 super()调用父类的方法
        print("say BBB")
b = B()
b.say()