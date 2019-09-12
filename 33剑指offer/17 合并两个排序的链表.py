'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减
规则。
'''
'''
要注意特殊输入，如果输入是空链表，不能崩溃。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None :
            return pHead2
        elif pHead2 == None:
            return pHead1
        pHead = None
        if pHead1.val <=pHead2.val:
            pHead = pHead1
            pHead.next = self.Merge(pHead1.next,pHead2)
        else:
            pHead = pHead2
            pHead.next = self.Merge(pHead1,pHead2.next)
        return pHead

