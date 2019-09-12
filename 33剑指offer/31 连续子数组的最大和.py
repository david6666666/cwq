'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计
算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的
正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的
最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''
'''
关键的问题在于成功分析整个过程。对于连续子数组，可以用一个数值来存储当前和，如果当前和小于零，那么在进行
到下一个元素的时候，直接把当前和赋值为下一个元素，如果当前和大于零，则累加下一个元素，同时用一个maxNum
存储最大值并随时更新。也可以利用动态规划解决。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here-
        if len(array) <=0 or array == None:
            return 0
        length = len(array)
        dp = [0] * length
        for i in range(length):
            if i == 0 or dp[i-1] <= 0:
                dp[i] = array[i]
            elif i != 0 and dp[i-1] > 0:
                dp[i] = dp[i-1] +array[i]
        return max(dp)

alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.FindGreatestSumOfSubArray(alist))