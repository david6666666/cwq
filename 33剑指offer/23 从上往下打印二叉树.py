'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''
'''
引入一个队列即可。推广：有向图的广度优先遍历也是基于队列的。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root == None:
            return []
        queue = []
        queue.append(root)
        result = []
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left :
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result