#工厂模式
# 设计模式是面向对象语言特有的内容，是我们在面临某一类问题时候固定的做法，设计
# 模式有很多种，比较流行的是：GOF（Goup Of Four）23 种设计模式。当然，我们没有
# 必要全部学习，学习几个常用的即可。
# 对于初学者，我们学习两个最常用的模式：工厂模式和单例模式。
# 工厂模式实现了创建者和调用者的分离，使用专门的工厂类将选择实现类、创建对象进
# 行统一的管理和控制。
class CarFactory:
    def createCar(self,brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == '比亚迪':
            return BYD()
        else:
            return "未知品牌，无法创建"
class Benz:
    pass
class BMW:
    pass
class BYD:
    pass

factory = CarFactory()
c1 = factory.createCar("奔驰")
c2 = factory.createCar("宝马")
print(c1)
print(c2)