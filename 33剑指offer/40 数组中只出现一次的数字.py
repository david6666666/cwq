'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
'''
任何一个数字异或他自己都等于0，0异或任何一个数都等于那个数。数组中出了两个数字之外，其他数
字都出现两次，那么我们从头到尾依次异或数组中的每个数，那么出现两次的数字都在整个过程中被抵
消掉，那两个不同的数字异或的值不为0，也就是说这两个数的异或值中至少某一位为1。我们找到结果数
字中最右边为1的那一位i，然后一次遍历数组中的数字，如果数字的第i位为1，则数字分到第一组，数
字的第i位不为1，则数字分到第二组。这样任何两个相同的数字就分到了一组，而两个不同的数字在第
i位必然一个为1一个不为1而分到不同的组，然后再对两个组依次进行异或操作，最后每一组得到的结果
对应的就是两个只出现一次的数字。
'''
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None or len(array) < 0 :
            return []
        result = 0
        for i in array:
            result ^= i
        index1 = self.FindFirstBitIs1(result)

        num1 = 0
        num2 = 0
        for j in range(len(array)):
            if self.isBit1(array[j],index1):
                num1 ^= array[j]
            else:
                num2 ^= array[j]
        return [num1, num2]

    def FindFirstBitIs1(self,num):
        index = 0
        while num & 1 == 0 and index <=32:
            index += 1
            num = num >> 1
        return index
    def isBit1(self,num,index):
        num = num >> index
        return num & 1