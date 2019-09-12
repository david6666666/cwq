'''
输入一个链表，输出该链表中倒数第k个结点。
'''
'''
代码的鲁棒性。需要注意：如果输入的链表为空；k大于链表的长度；k为0的情况。对于正常情况，设
置两个指针分别指向头结点，第一个指针向前走k-1步，走到正数第k个结点，同时保持第二个指针不动
，然后第一个指针和第二个指针每次同时前移一步，这样第一个指针指向尾结点的时候，第二个指针指向
倒数第k个结点。判断尾结点的条件是 pNode.next == None。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k<=0:
            return None

        preNode = head
        curNode = head
        for i in range(k-1):
            if curNode.next != None:
                curNode = curNode.next
            else:
                return None
        while curNode.next!=None:
            curNode = curNode.next
            preNode = preNode.next
        return preNode

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
print(S.FindKthToTail(node1, 3).val)