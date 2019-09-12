'''
给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0]
,k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们
把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
'''
'''
动态规划：
定义函数f(n)为乘积最大值，递推函数为f(n) = max(f(i)*f(n-i)) 0<i<n。至下而上,子问题的
最优解存在数组products里,数组中第i个元素表示长度为i的绳子剪成若干段之后各段长度乘积的
最大值。
贪婪算法：
当n>=5时，尽可能多剪长度为3的绳子，如果n=4把绳子剪成两个长度为2的绳子
'''
# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number <2:
            return 0
        elif number == 2:
            return 1
        elif number == 3:
            return 2
        products = [0] * (number+1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4,number+1):
            max = 0
            for j in range(1,i//2+1):
                temp = products[j] * products[i-j]
                if max < temp:
                    max = temp
                products[i] = max
        max = products[number]
        return max

    def cutRope2(self, number):
        if number <2:
            return 0
        elif number == 2:
            return 1
        elif number == 3:
            return 2
        timesOf3 = number//3

        if number - timesOf3*3 == 1:
            timesOf3 -= 1
        timesOf2 = (number - timesOf3*3) //2
        return (3**timesOf3 ) * (2**timesOf2)
S = Solution()
print(S.cutRope2(9))