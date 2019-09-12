'''
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

'''
我们需要设置一个指针preNode，preNode最开始为None，然后设置两个指针，pNode指
向当前节点，pNext指向pNode下一个结点，⓵如果pNext不为空而且pNext的值等
于pNode的值，那么就说明出现了重复数字的结点，就需要删除，然后从pNode开始遍
历，如果结点值等于前面那个重复值，继续遍历。当遍历到None或者不同值结点的时候
，这时候需要判断preNode结点，如果preNode结点为None，就说明我们刚才的重复结点
是从整个链表的头结点开始重复的，就直接把pHead设置为当前结点，pNode也设置为当
前结点。反之，如果preNode不为None，直接把preNode的下一个指针指向当前节点，
pNode指向preNode即可；⓶如果pNext为空或者pNext的值不等于pNode的值，说明当前
的这个pNode和后面的值不重复，直接令preNode = pNode，pNode指向下一个结点即可。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        pre_head = ListNode(-1)
        pre_p = pre_head
        cur_p = pHead
        while cur_p and cur_p.next:
            if cur_p.val == cur_p.next.val:
                delete_value = cur_p.val
                while cur_p and cur_p.val == delete_value:
                    cur_p = cur_p.next
                pre_p.next = cur_p
            else:
                pre_p.next = cur_p
                pre_p = pre_p.next
                cur_p = cur_p.next
        return pre_p.next