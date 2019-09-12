'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''
'''
这道题的关键也在于讨论清楚情况，把所有可能出现的情况都考虑到。需要注意的是，指数E
后面必须跟一个整数，不能没有数，也不能为小数。
'''
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        if s == None or len(s) <= 0:
            return False
        aList = [w.lower() for w in s]
        if 'e' in aList:
            indexE = aList.index('e')
            front = aList[:indexE]
            behind = aList[indexE+1:]
            if '.' in behind or len(behind) == 0:
                return False
            isFront = self.scanDigit(front)
            isBehind = self.scanDigit(behind)
            return isBehind and isFront
        else:
            isNum = self.scanDigit(aList)
            return isNum

    def scanDigit(self, alist):
        dotNum = 0
        allowVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
        for i in range(len(alist)):
            if alist[i] not in allowVal:
                return False
            if alist[i] == '.':
                dotNum += 1
            if alist[i] in '+-' and i != 0:
                return False
        if dotNum > 1:
            return False
        return True

s = Solution()
print(s.isNumeric('17.'))