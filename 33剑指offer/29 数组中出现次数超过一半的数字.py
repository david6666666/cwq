'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于
数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
'''
两种思路。第一种思路，出现次数超过一半的数字，不管如何，必然这个数字位于数组中间的位置，因此可以采用类似
于快排的划分的方法，找到位于数组中间的位置的数字，然后在顺序检索是否这个数字出现次数超过一半。第二种思路
根据数组的特点，出现次数超过一半的数，他出现的次数比其他数字出现的总和还要多，因此可以最开始保存两个数值
：数组中的一个数字以及它出现的次数，然后遍历，如果下一个数字等于这个数字，那么次数加一，如果不等，次数
减一，当次数等于0的时候，在下一个数字的时候重新复制新的数字以及出现的次数置为1，直到进行到最后，然后再
验证最后留下的数字是否出现次数超过一半，因为可能前面的次数依次抵消掉，最后一个数字就直接是保留下来的数
字，但是出现次数不一定超过一半。
'''
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        if numbers == None or length <= 0:
            return 0
        result = numbers[0]
        times = 1
        for i in range(1,length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.CheckMoreThanHalf(numbers,length,result):
            result = 0
        return result
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times*2 <= length:
            return False
        return True