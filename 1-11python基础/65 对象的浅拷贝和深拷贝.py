#测试对象的引用赋值、浅拷贝、深拷贝
import copy
class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen
class CPU:
    def calculate(self):
        print("计算，算个 12345")
        print("CPU 对象:", self)

class Screen:
    def show(self):

        print("显示一个好看的画面，亮瞎你的钛合金大眼")
        print("屏幕对象：", self)
c = CPU()
s = Screen()
m = MobilePhone(c, s)
m.cpu.calculate()
n = m  # 两个变量，但是指向了同一个对象
print(m, n)
m2 = copy.copy(m)  # m2 是新拷贝的另一个手机对象
print(m, m2)
m.cpu.calculate()
m2.cpu.calculate()  # m2 和 m 拥有了一样的 cpu 对象和 screen 对象
m3 = copy.deepcopy(m)
m3.cpu.calculate()  # m3 和 m 拥有不一样的 cpu 对象和 screen
# 对象