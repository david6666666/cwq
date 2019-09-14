class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic={root:None}
        def bfs(node):
            if node:
                if node.left:dic[node.left]=node
                if node.right:dic[node.right]=node
                bfs(node.left)
                bfs(node.right)
        bfs(root)
        l1,l2=p,q
        while(l1!=l2):
            l1=dic.get(l1) if l1 else q
            l2=dic.get(l2) if l2 else p
        return l1
