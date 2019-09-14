# 二叉树的最低公共祖先
"""
Definition of TreeNode:
"""
'''
首先来看比较简单的情况--二叉搜索树的最低公共祖先，对于二叉搜索树而言，每个节点的左子节点都小于这个数
，右子节点都大于这个数，因此，我们比较当前节点和需要比较的结点m，n的大小，如果当前节点的值均大于m，
n，则在当前节点的左子树继续操作，如果当前节点均小于m，n，则在当前节点的右子树继续操作，反之，则当前
结点是最小公共祖先。而对于普通的二叉树而言，我们如果希望找到两个结点的最低公共祖先，那么我们可以先
从树的根节点开始，找到根节点到结点m和结点n的路径，这时候我们就有两个List或者两个链表，然后就像前面
题中遇到的寻找两个链表的公共结点一样，从后往前遍历两个List找到最靠后的第一个公共结点即可。
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def __init__(self):
        self.stack = []
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root == None:
            return False
        pathA = self.storeNodes(root, A)[0]
        pathB = self.storeNodes(root, B)[0]
        if pathA and pathB:
            lenA, lenB = len(pathA), len(pathB)
            diff = abs(lenA - lenB)
            if lenA > lenB:
                markA = lenA - diff - 1
                markB = lenB - 1
            else:
                markA = lenA - 1
                markB = lenB - diff - 1
            while markA >= 0 and markB >= 0:
                if pathA[markA] == pathB[markB]:
                    return pathA[markA]
                markA -= 1
                markB -= 1

    def storeNodes(self, root, targetNode):
        if root == None or targetNode == None:
            return []
        elif root.val == targetNode.val:
            return [[targetNode]]
        stack = []
        if root.left:
            stackLeft = self.storeNodes(root.left, targetNode)
            for i in stackLeft:
                i.insert(0, root)
                stack.append(i)
        if root.right:
            stackRight = self.storeNodes(root.right, targetNode)
            for i in stackRight:
                i.insert(0, root)
                stack.append(i)
        return stack


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
S = Solution()
print(S.lowestCommonAncestor(pNode1, pNode4,pNode5))
