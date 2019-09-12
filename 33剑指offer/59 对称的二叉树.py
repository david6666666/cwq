'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像
是同样的，定义其为对称的。
'''
'''
分为递归和非递归的两种方式，思想是一样的。主要就是把叶子节点的None节点也加入到遍
历当中。按照前序遍历二叉树，存入一个序列中。然后按照和前序遍历对应的先父节点，然
后右子节点，最后左子节点遍历二叉树，存入一个序列。如果前后两个序列相等，那么说明
二叉树是对称的。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymmetricalCore(pRoot,pRoot)

    def isSymmetricalCore(self,pRoot1,pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetricalCore(pRoot1.left,pRoot2.right) and \
               self.isSymmetricalCore(pRoot1.right,pRoot2.left)

