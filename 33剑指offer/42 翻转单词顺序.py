'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多
对数字的和等于S，输出两个数的乘积最小的。
'''
'''
首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后从前往后依次遍历新字符串，如果遇到空
格，就把空格前的字符串用reverse翻转，添加空格，继续遍历。需要注意的是，如果新字符串结尾不是空格，
当遍历到结尾的时候，前一个空格到结尾的字符串没有翻转，因此记得跳出遍历后，需要再完成一次翻转操作。
'''
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        if s == None or len(s)<0:
            return
        s1 = s[::-1]
        arr = s1.split(' ')
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        ss = ' '.join(arr)
        return ss
S = Solution()
print(S.ReverseSentence('I am a student.'))