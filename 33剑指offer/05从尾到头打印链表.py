'''
输入一个链表，从尾到头打印链表每个节点的值。
'''
'''
从头到尾遍历链表，并用一个栈存储每个结点的值，之后出栈输出值即可。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        list  = []
        while(listNode):
            list.insert(0,listNode.val)
            listNode = listNode.next
        return list

