'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''
'''
后序遍历二叉树的每个节点，遍历到一个节点之前就遍历了它的左右子树。遍历的时候记录深度，就可以
一边遍历一边判断每个节点是否平衡
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)
        return self.flag

    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        left = 1+self.getDepth(pRoot.left)
        right = 1+self.getDepth(pRoot.right)

        if abs(left - right) > 1:
            self.flag = False
        return left if left>right else right
pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

S = Solution()
print(S.IsBalanced_Solution(pNode1))