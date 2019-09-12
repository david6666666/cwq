'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''
'''
先遍历一遍字符串，用一个hash表存放每个出现的字符和字符出现的次数。再遍历一遍字符串，找到hash值等于1的输出即可。
'''


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == None or len(s) <= 0:
            return -1
        length = len(s)
        dic = {}
        for i in range(length):
            dic[s[i]] = dic.get(s[i],0) + 1
        for i in range(length):
            if dic[s[i]] == 1:
                return i

s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))