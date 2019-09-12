'''
一个链表中包含环，请找出该链表的环的入口结点。
'''
'''
寻找链表中环的入口结点主要分成三个步骤：首先是设置两个快慢指针，如果快慢指针相遇，则快慢指针
必然都在环中；然后从相遇的地方设置一个指针向后遍历并记录走的步数，当这个指针重新指到开始的位
置的时候，当前对应的步数就是环中结点的数量k；然后设置两个指针从链表开始，第一个节点先走k步，然
后第二个指针指到链表的开始，两个指针每次都向后走一步，两个指针相遇的位置就是链表的入口。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        has_loop,num_loop = self.find_loop(pHead)
        if not num_loop:
            return None
        p1 = pHead
        p2 = pHead
        while num_loop:
            p1 = p1.next
            num_loop -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
    def find_loop(self,pHead):
        if pHead == None:
            return False,None
        p1 = pHead
        p2 = pHead
        while True:
            #p1走两步
            for _ in range(2):
                if p1.next == None:
                    return False,None
                p1 = p1.next
            #p2走一步
            p2 = p2.next
            if p1 == p2:
                break
        num_loop = 0
        while True:
            p2 = p2.next
            num_loop += 1
            if p2 == p1:
                return True,num_loop
