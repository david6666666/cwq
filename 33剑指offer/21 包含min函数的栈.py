'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
（时间复杂度应为O（1））。
'''
'''
引入两个栈，一个栈每次push实际的数字，另一个minStack，如果push的数字小于minStack栈顶
的数字，push新的数字，繁殖，把栈顶的数字再压入一遍。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            temp = self.min()
            self.minstack.append(temp)
    def pop(self):
        # write code here
        if self.stack == [] or self.minstack == []:
            return None
        self.stack.pop()
        self.minstack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]