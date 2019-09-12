'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
'''
依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []
    def Permutation(self, arr):
        if not arr:
            return []
        arr = list(arr)
        position = 0
        end = len(arr)
        return self.permutation(arr, position, end)
    def permutation(self,arr, position, end):
        if position == end:
            sss = ''.join([str(x) for x in arr])
            self.res.append(sss)
        else:
            for index in range(position, end):
                if self.isduplicate(arr, position, index):  # 如果位置n出现过数字li[i]，跳过
                    continue
                arr[index], arr[position] = arr[position], arr[index]
                self.permutation(arr, position+1, end)
                arr[index], arr[position] = arr[position], arr[index]
        return sorted(self.res)
    def isduplicate(self,arr, n, t):
        """
        从arr的位置n到位置t-1，有没有和li[t]相等的数字
        """
        while n < t:
            if arr[n] == arr[t]:
                return True
            n += 1
        return False

ss = 'acba'
S = Solution()
print(S.Permutation(ss))