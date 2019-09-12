# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        return self.sumN(n)

    def sum0(self, n):
        return 0

    # 利用非0值作两次非运算返回false, 0作两次非运算返回True
    def sumN(self, n):
        fun = {False: self.sum0, True: self.sumN}
        # 此处的fun[not not n] 不能写作func[not not n-1], 否则测试用例为0的话, 就会无限次迭代
        return n + fun[not not n](n - 1)
