'''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数
值大小顺序第三小结点的值为4。
'''
'''
中序遍历二叉搜索树，返回第k个值
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.treeNode = []
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot == None or k == 0:
            return
        self.InOrder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k-1]
    def InOrder(self,pRoot):
        if len(self.treeNode) < 0:
            return None
        if pRoot.left:
            self.InOrder(pRoot.left)
        self.treeNode.append(pRoot)
        if pRoot.right:
            self.InOrder(pRoot.right)
