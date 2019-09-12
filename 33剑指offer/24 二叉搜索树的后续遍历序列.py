'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''
'''
根据后续遍历的性质，尾元素必定是树的根，同时小于尾元素的值是左子树，大于尾元素的
值为右子树，且序列前半部分均小于尾元素，后半部分均大于尾元素（如果同时存在左右子
树的话），可以将序列划分左子树序列和右子树序列，然后递归比较师妹每一段均满足此
性质。可以减少递归深度的办法：某段的元素个数如果<=3，则返回True；某整段的最小元素
不小于尾元素或者整段的最大元素不大于尾元素，说明仅有左子树或者右子树，返
回True。
'''
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return []
        index = 0
        root = sequence[-1]
        length = len(sequence)
        for i in range(length-1):
            index = i
            if sequence[index] > root:
                break
        for j in range(index+1,length-1):
            if sequence[j] < root:
                return False
        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if index <length-1:
            right = self.VerifySquenceOfBST(sequence[index:length-1])
        return left and right