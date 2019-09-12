'''
输入两个链表，找出它们的第一个公共结点。
'''
'''
首先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，那么我们就先让长度为m的链表走
m-n个结点，然后两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。


'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = self.getLen(pHead1)
        len2 = self.getLen(pHead2)
        cha = abs(len1 - len2)
        if len1 >len2:
            pHeadLong = pHead1
            pHeadShort = pHead2
        else:
            pHeadLong = pHead2
            pHeadShort = pHead1
        for i in range(cha):
            pHeadLong = pHeadLong.next
        while pHeadLong != None and pHeadShort != None and pHeadLong != pHeadShort:
            pHeadLong = pHeadLong.next
            pHeadShort = pHeadShort.next
        pCommon = pHeadLong
        return pCommon

    def getLen(self,pHead):
        len = 0
        while pHead != None:
            len += 1
            pHead = pHead.next
        return len