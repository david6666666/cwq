'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # 将1-n全部转换为字符串
        # 只需要统计每个字符串中'1'出现的次数并相加即可
        count = 0
        base = 1
        round = n
        while round >0:
            weight = round % 10
            round //= 10
            count = count + round * base
            if weight == 1:
                count += (n%base) +1
            elif weight >1:
                count += base
            base *= 10
        return count
S = Solution()
print(S.NumberOf1Between1AndN_Solution(514))
