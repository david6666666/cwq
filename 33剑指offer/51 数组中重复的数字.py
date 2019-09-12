# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    #对于一个长度为n的数组里所有的数字都在0到n-1的范围内。查找重复数字的话，首先
    # 容易想到，对数组进行排序，然后遍历数组查找重复的数字，这样的时间复杂度为
    # O(nlogn)；或者建立一个哈希表，这样实在O(n)的时间查找到，但是空间复杂度O(n)。
    # 另外一个空间复杂度为O(1)的算法如下，因为数字在0~n-1的范围内，那么如果数字
    # 没有重复，那么当数组排序之后数字i将出现在下标为i的位置，但是有重复的话，
    # 在某个位置j出现的数字将不是j。我们重排这个数组。从头到尾依次扫描这个数组
    # 中的每个数字，如果下标i不是出现数字i，那么就把数字i和i处的数字进行交换使数
    # 字i出现在应该出现的位置，如果新交换的数字还不是他应该出现的位置，继续交换
    # ，直至该处的数字m等于x下标m，如果在交换的过程中，第i处的位置数字等于第m处
    # 的数字，那么我们就找到了第一个重复的数字，记录这个数字，在从下一个位置继续
    # 扫描。
    # 输出所有重复的数字
    def duplicate(self, numbers, duplication):
        if numbers == None or len(numbers) <= 0:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers) - 1:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]

        return False


test = [2, 3, 1, 0, 2, 5, 3]
s = Solution()
dupulication = [0]
print(s.duplicate(test, dupulication))
