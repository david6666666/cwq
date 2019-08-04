# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        find  = False
        row = 0
        column = len(array)-1

        while(row<len(array[0]) and  column >=0):
            if array[row][column] == target:
                find = True
                break
            elif array[row][column] > target:
                column -=1
            else:
                 row +=1
        return find




