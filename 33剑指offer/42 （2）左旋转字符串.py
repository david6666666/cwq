'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果
。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出
循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
'''
'''
首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后根据题目中给出的左旋转字符串的个
数n，用全字符串长度length减去旋转字符串个数n，求得对于新的字符串应该在哪一位进行旋转，然后分
别旋转前[:length-n]子串和[length-n:]子串，重新拼接两个子串即可。
'''
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if len(s) <= 0 or len(s) < n or n < 0:
            return ''
        strList= list(s)
        self.Reverse(strList)
        length = len(s)
        pivot = length - n
        frontList = self.Reverse(strList[:pivot])
        behindList = self.Reverse(strList[pivot:])
        resultStr = ''.join(frontList) + ''.join(behindList)
        return resultStr

    def Reverse(self, alist):
        if alist == None or len(alist) <= 0:
            return ''
        startIndex = 0
        endIndex = len(alist) - 1
        while startIndex < endIndex:
            alist[startIndex], alist[endIndex] = alist[endIndex], alist[startIndex]
            startIndex += 1
            endIndex -= 1
        return alist

test = 'abcdefg'
s = Solution()
print(s.LeftRotateString(test, 2))