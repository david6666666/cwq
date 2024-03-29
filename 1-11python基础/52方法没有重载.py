'''
在其他语言中，可以定义多个重名的方法，只要保证方法签名唯一即可。方法签名包含 3
个部分：方法名、参数数量、参数类型。

Python 中，方法的的参数没有声明类型（调用时确定参数的类型），参数的数量也可以由
可变参数控制。因此，Python 中是没有方法的重载的。定义一个方法即可有多种调用方式，
相当于实现了其他语言中的方法的重载。

如果我们在类体中定义了多个重名的方法，只有最后一个方法有效。
建议：不要使用重名的方法！Python 中方法没有重载。
'''