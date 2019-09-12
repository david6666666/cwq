'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等
于S，输出两个数的乘积最小的。
'''
'''
设定两个指针，一个指向数组的起点，一个指向数组的终点，然后对两个数字求和，如果和大于目标值
，则把后一个指针前移，如果和小于目标值，则把前一个指针后移。两个指针交汇的时候如果还没找到
，就终止操作。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if array == None or len(array) <0:
            return []
        left = 0
        right = len(array) - 1
        while left < right :
            if array[left] + array[right] > tsum:
                right -= 1
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                return [array[left], array[right]]
        return []
test = [1,2,4,7,11,15]
s = Solution()
print(s.FindNumbersWithSum(test, 15))