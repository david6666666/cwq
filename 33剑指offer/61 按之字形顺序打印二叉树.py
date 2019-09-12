'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的
顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
'''
使用两个队列，与一个标志位来标记是否从左至右存。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        levels, result, leftToRight = [pRoot], [], True
        while len(levels) > 0:
            curLev,nextLev = [], []
            for node in levels:
                curLev.append(node.val)
                if node.left:
                    nextLev.append(node.left)
                if node.right:
                    nextLev.append(node.right)
            if not leftToRight:
                curLev.reverse()
            if curLev:
                result.append(curLev)
            levels = nextLev
            leftToRight = not leftToRight
        return result

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