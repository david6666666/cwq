# Python 支持多重继承，一个子类可以有多个“直接父类”。这样，就具备了“多个父
# 类”的特点。但是由于，这样会被“类的整体层次”搞的异常复杂，尽量避免使用。

class A:
    def aa(self):
        print("aa")
class B:
    def bb(self):
        print("bb")
class C(B,A):
    def cc(self):
        print("cc")
c = C()
c.cc()
c.bb()
c.aa()