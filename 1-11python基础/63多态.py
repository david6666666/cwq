# 多态（polymorphism）是指同一个方法调用由于对象不同可能会产生不同的行为。在现实
# 生活中，我们有很多例子。比如：同样是调用人的休息方法，张三的休息是睡觉，李四的休
# 息是玩游戏，高淇老师是敲代码。同样是吃饭的方法，中国人用筷子吃饭，英国人用刀叉吃
# 饭，印度人用手吃饭。
# 关于多态要注意以下 2 点：
# 1. 多态是方法的多态，属性没有多态。
# 2. 多态的存在有 2 个必要条件：继承、方法重写。

class Animal:
    def shout(self):
        print("动物叫了一声")
class Dog(Animal):
    def shout(self):
        print("小狗，汪汪汪")
class Cat(Animal):
    def shout(self):
        print("小猫，喵喵喵")
def animalShout(a):
    if isinstance(a,Animal):
        a.shout() #传入的对象不同，shout 方法对应的实际行为也不同。
animalShout(Dog())
animalShout(Cat())