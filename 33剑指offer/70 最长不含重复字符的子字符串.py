'''
给定一个字符串，找出不含有重复字符的最长子串的长度。
'''
'''
用动态规划来做。首先定义f(i)表示以第i个字符结尾的不包含重复字符的子字符串的最长长度。

如果第i个字符之前没有出现过，那么f(i)=f（i-1)+1。

如果第i个字符之前出现过，讲该字符与上次出现的字符串中的位置的距离记为d，分两种情况：

    d<=f(i-1)，说明第i个字符之前出现的字符在当前子字符串内，则f(i)=d

    d>f(i-1），说明之前出现的字符在当前子字符串外，f(i)=f(i-1)+1

'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        curLength = 0
        maxLength = 0
        position = [-1] *256
        for i in range(len(s)):
            preIndex = position[ord(s[i])]
            d = i - preIndex
            if preIndex < 0 or d > curLength:
                curLength += 1
            else:
                if curLength > maxLength:
                    maxLength = curLength
                curLength = d
            position[ord(s[i])] = i
        if curLength > maxLength:
            maxLength = curLength
        return maxLength

S = Solution()
print(S.lengthOfLongestSubstring('arabcacfr'))

