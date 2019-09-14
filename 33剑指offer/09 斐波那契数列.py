'''
如何不使用递归实现斐波那契数列，需要把前面两个数字存入在一个数组中。斐波那契数列
的变形有很多，如青蛙跳台阶，一次跳一个或者两个；铺瓷砖问题。变态青蛙跳，每次至少
跳一个，至多跳n个，一共有f(n)=2n-1种跳法。考察数学建模的能力。矩形覆盖也是一个
斐波那契数列问题
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]
    # 青蛙跳台阶, 每次可以跳1级或2级
    def jumpFloor(self, number):
        # write code here
        Arr = [1, 2]
        if number < 3:
            return Arr[number - 1]
        if number >= 3:
            for i in range(3, number + 1):
                Arr.append(Arr[i - 2] + Arr[i - 3])
        return Arr[number - 1]

    def jumpFloorII(self, number):
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans

test = Solution()
print(test.Fibonacci(100))
print(test.jumpFloor(3))
print(test.jumpFloorII(2))