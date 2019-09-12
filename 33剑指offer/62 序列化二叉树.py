'''
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而
使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍
历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！
 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
'''
'''
最终要实现的是二叉树的序列化和反序列化。首先来看二叉树的序列化，二叉树的序列化就
是采用前序遍历二叉树输出节点，再碰到左子节点或者右子节点为None的时候输出一个特殊
字符"#"。对于反序列化，就是针对输入的一个序列构建一棵二叉树，我们可以设置一个指针
先指向序列的最开始，然后把指针指向位置的数字转化为二叉树的结点，后移一个数字，继
续转化为左子树和右子树。当遇到当前指向的字符为特殊字符"#"或者指针超出了序列的长度
，则返回None，指针后移，继续遍历。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.stream = ''
    def Serialize(self, root):
    # write code here

        if root is None:
            self.stream = self.stream + '#,'
            return
        self.stream = self.stream +str(root.val)+','
        self.Serialize(root.left)
        self.Serialize(root.right)
        return self.stream[:-1]

    def Deserialize(self, s):
        if s is None:
            return
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree

    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None,sp+1
        node = TreeNode(int(s[sp]))
        sp+=1
        node.left, sp = self.deserialize(s,sp)
        node.right, sp = self.deserialize(s,sp)
        return node, sp