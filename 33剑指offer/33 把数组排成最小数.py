'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组
{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
'''
首先将数组中的数字全部转换为字符串存储在一个新的数组中，然后比较每两个数字串的拼接的mn和nm的大小
，若mn<nm，则m更小，反之n更小，然后把更小的数放入一个新的List中，最后输出即可。使用冒泡排序很方便。
'''
from functools import cmp_to_key
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return ''
        strList = []
        for i in numbers:
            strList.append(str(i))
        # key是一种比较规则
        # 比较 x+y 和 x-y 的大小, 因为为str型, 需要先转换成int型
        key = cmp_to_key(lambda x,y: int(x+y) - int(y+x))
        strList.sort(key=key)
        return ''.join(strList)

numbers = [3, 32, 321]
s = Solution()
print(s.PrintMinNumber(numbers))