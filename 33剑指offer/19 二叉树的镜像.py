'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''
'''
先序遍历树的每个节点，如果遍历到的节点有子节点，就交换两个子节点。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return
        if root.left == None and root.right == None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left != None:
            self.Mirror(root.left)
        if root.right != None:
            self.Mirror(root.right)