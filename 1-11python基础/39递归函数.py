'''
递归函数指的是：自己调用自己的函数，在函数体内部直接或间接的自己调用自己。递归类
似于大家中学数学学习过的“数学归纳法”。 每个递归函数必须包含两个部分：

    1. 终止条件
        表示递归什么时候结束。一般用于返回值，不再调用自己。
    2. 递归步骤
        把第 n 步的值和第 n-1 步相关联。

递归函数由于会创建大量的函数对象、过量的消耗内存和运算能力。在处理大量数据时，谨
慎使用。
'''


def test01(n):
    print("test01",n)
    if n==0:
        print("over")
    else:
        test01(n-1)

    print("test01***",n)

test01(4)
print()

#阶乘计算
def factorial(n):
    if n==1:return 1
    return n*factorial(n-1)
for i in range(1,6):
    print(i,'!=',factorial(i))