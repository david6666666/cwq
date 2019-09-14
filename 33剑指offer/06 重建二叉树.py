'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
'''
利用二叉树前序遍历和中序遍历的特性。前序遍历的第一个值一定为根节点，对应于中序
遍历中间的一个点。在中序遍历序列中，这个点左侧的均为根的左子树，这个点右侧的均
为根的右子树。这时可以利用递归，分别取前序遍历[1:i+1]和中序遍历的[:i]对应与左
子树继续上一个过程，取前序遍历[i+1:]和中序遍历[i+1]对应于右子树继续上一个过
程，最终得以重建二叉树。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None
        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1],tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:],tin[i+1:])
        return root

pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)