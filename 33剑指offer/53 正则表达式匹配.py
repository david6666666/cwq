'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''

# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        pat = pattern
        if len(s)==0 and len(pat)==0:
            return True
        if len(s)>0 and len(pat)==0:
            return False
        if len(pat)>1 and pat[1]=='*':
            if len(s)>0 and (s[0]==pat[0] or pat[0]=='.'):  # ab  .*  / ab a*  两种情况统一处理
                return self.match(s[1:], pat) or self.match(s, pat[2:]) or \
                       self.match(s[1:], pat[2:])  # *匹配1个保持当前模式/不匹配/移动到下一个状态
            else:  # len(s)==0 s匹配完，看剩下的是否匹配
                return self.match(s, pat[2:])
        if len(s)>0 and (pat[0]=='.' or pat[0]==s[0]):  # 处理非匹配字符和 . 直接处理下一个
            return self.match(s[1:], pat[1:])