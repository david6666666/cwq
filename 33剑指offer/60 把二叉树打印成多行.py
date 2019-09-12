'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
'''
引入两个队列。首先把当前层的节点存入到一个队列queue1中，然后遍历当前队列queue1，
在遍历的过程中，如果节点有左子树或右子树，依次存入另一个队列queue2。然后遍历队
列queue2，如此往复。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    #引入两个队列。首先把当前层的节点存入到一个队列queue1中，然后遍历当前队
    # 列queue1，在遍历的过程中，如果节点有左子树或右子树，依次存入另一个
    # 队列queue2。然后遍历队列queue2，如此往复。
    def Print(self, pRoot):
        if pRoot == None:
            return []
        nodes, res= [pRoot], []
        while nodes:
            currentQueue = []
            nextQueue = []
            for node in nodes:
                currentQueue.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            res.append(currentQueue)
            nodes = nextQueue
        return res


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
aList = S.Print(pNode1)
print(aList)