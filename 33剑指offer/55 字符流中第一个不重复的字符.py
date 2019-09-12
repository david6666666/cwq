'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现
一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''
'''
引入两个辅助存储空间。一个Dict存储当前出现的字符以及字符出现的次数，一个List存储当前出现字符。然
后每次比较List的第一个字符在Dict中对应的次数，如果为1则输出这个字符，如果不为1则弹出这个字符比较
下一个字符。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.adict = {}
        self.alist = []
    def FirstAppearingOnce(self):
        while len(self.alist) > 0 and self.adict[self.alist[0]] == 2:
            self.alist.pop(0)
        if len(self.alist) == 0:
            return '#'
        else:
            return self.alist[0]
    def Insert(self, char):
        if char not in self.adict.keys():
            self.adict[char] = 1
            self.alist.append(char)
        elif self.adict[char]:
            self.adict[char] = 2
