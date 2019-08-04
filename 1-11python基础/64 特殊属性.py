#测试特殊属性
class A:
    pass
class B:
    pass
class C(B,A):
    def __init__(self,nn):
        self.nn = nn
    def cc(self):
        print("cc")
c = C(3)
print(dir(c))
print(c.__dict__)
print(c.__class__)
print(C.__bases__)
print(C.mro())
print(A.__subclasses__())