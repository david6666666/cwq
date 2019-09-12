'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
'''
当要删除的结点不是尾结点而且不是仅有一个结点的头结点，可以把该结点i的下一个
结点j的内容复制到结点i，同时把i结点的next指向j结点的next，然后再删除结点j。
如果要删除的链表为单结点链表且待删除的结点就是头结点，需要把头结点置为None，
如果删除的结点为链表的尾结点，那么就需要顺序遍历链表，找到尾节点前面一个结点
，然后将其next置空。
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None

class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if pListHead == None or pToBeDeleted == None:
            return None
        if pToBeDeleted.next != None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext.next
            pNext.__del__()
        elif pListHead == pToBeDeleted:
            pListHead.__del__()
            pToBeDeleted.__del__()
        else:
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
S.DeleteNode(node1, node3)
print(node3.val)
S.DeleteNode(node1, node3)
print(node3.val)
print(node2.val)
S.DeleteNode(node1, node1)
print(node1.val)
S.DeleteNode(node1, node1)
print(node1.val)