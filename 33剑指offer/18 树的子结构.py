'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''
'''
第一步，在树A中找到和树B的根节点一样的节点R；第二步，判断树A中以R为根节点的子树
是不是包含和树B一样的结构
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result  = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)
        return result
    def DoesTree1haveTree2(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return  self.DoesTree1haveTree2(pRoot1.left,pRoot2.left) and \
                self.DoesTree1haveTree2(pRoot1.right,pRoot2.right)