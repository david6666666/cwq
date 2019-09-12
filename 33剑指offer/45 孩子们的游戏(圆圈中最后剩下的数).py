'''
0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
求这个圆圈中最后剩下的一个数字
'''
# -*- coding:utf-8 -*-
class Solution:
    # #环形链表解决
    # def LastRemaining_Solution(self, n, m):
    #     if n <= 0 or m <= 0:
    #         return -1
    #     circle = list(range(n))
    #     current = 0
    #     while len(circle) > 1:
    #         for i in range(1,m):
    #             if current == len(circle)  :
    #                 current = 0
    #             current += 1
    #             if current >= len(circle) :
    #                 current = 0
    #         circle.pop(current)
    #     return circle[0]
# 方法二：数学推导规律
#
# 　　n个数字的圆圈，不断删除第m个数字，我们把最后剩下的数字记为f(n,m)。
#
# 　　n个数字中第一个被删除的数字是(m-1)%n， 我们记作k，k=(m-1)%n。
#
# 　　那么剩下的n-1个数字就变成了：0,1,……k-1,k+1,……,n-1，我们把下一轮第一个数字排在最前面，并且将这个长度为n-1的数组映射到0~n-2。
#
# 　　原始数字：k+1,……,   n-1,       0,    1,……k-1
#
# 　　映射数字：0    ,……,n-k-2, n-k-1, n-k,……n-2
#
# 　　把映射数字记为x，原始数字记为y，那么映射数字变回原始数字的公式为 y=(x+k+1)%n。
#
# 　　在映射数字中，n-1个数字，不断删除第m个数字，由定义可以知道，最后剩下的数字为f(n-1,m)。我们把它变回原始数字，由上一个公式可以得到最后剩下的原始数字是（f(n-1,m)+k+1)%n，而这个数字就是也就是一开始我们标记为的f(n,m)，所以可以推得递归公式如下：
#
# 　　　　　　　　　　f(n,m) =（f(n-1,m)+k+1)%n
#
# 　　将k=(m-1)%n代入，化简得到：
#
# 　　　　　　　　　　f(n,m) =（f(n-1,m)+m)%n
#
# 　　　　　　　　　　f(1,m) = 0
#
# 　　代码中可以采用循环或者递归的方法实现该递归公式。时间复杂度为O(n)，空间复杂度为O(1)。
    def LastRemaining_Solution(self, n, m):
        if n <1 or m < 1:
            return  -1
        remainIndex = 0
        for i in range(2, n+1):
            remainIndex = (remainIndex + m)% i
        return remainIndex
S = Solution()
print(S.LastRemaining_Solution(5,3))
