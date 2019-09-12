'''
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他
随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以
看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4)
,“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气
如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
'''
'''
先置换特殊字符AJQK为数字，排序，然后求出大小王即0的个数，然后求出除去0之外的，数组间的数字间
隔(求间隔的时候记得减去1，比如4和5的间隔为5-4-1，表示4和5是连续的数字)，同时求间隔的时候需要
鉴别是否出现对。最后比较0的个数和间隔的大小即可
'''
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return False
        transDict = {'A':1, 'J':11, 'Q':12, 'K':13}
        for i in range(len(numbers)):
            if numbers[i] in transDict.keys():
                numbers[i] = transDict[numbers[i]]
        numbers = sorted(numbers)
        numbersOfZero = 0
        numbersOfGap = 0
        #统计0的个数
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            numbersOfZero += 1
            i += 1
        #统计间隔的个数
        left = numbersOfZero
        right = left + 1
        while right < len(numbers):
            if numbers[left] == numbers[right]:
                return False
            numbersOfGap += numbers[right] - numbers[left] - 1
            left = right
            right += 1
        return False if numbersOfGap > numbersOfZero else True