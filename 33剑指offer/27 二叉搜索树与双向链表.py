'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
'''
其实这段代码也就5行，5行中2行是中序遍历的代码，分别是第25、33行；3行是更改节点指
向的代码，为30-32行。26-28行的if语句只有在中序遍历到第一个节点时调用，自此之后
listHead不变，listTail跟随算法的进度。为了更清楚的展示，给出中序遍历的代码如下。
对比可以看出来，实际上只是中序遍历中的第八行代码被上述的if-else语句替代了，仅
此而已。

'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead == None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead

