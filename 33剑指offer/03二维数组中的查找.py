'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
'''
对于在一个每一行从右到左依次递减，每一列从上到下依次递增的二维数组查找一个元
素，可以选择从数组右上角开始查找array[i][j]，如果array[i][j]大于目标元素，
j-=1，如果array[i][j]小于元素，i+=1，依次循环直至找到这个数。
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = 0
        column = len(array[0]) - 1
        while row <len(array) and column >=0 :
            if array[row][column] ==target:
                return True
            elif array[row][column] > target:
                column -= 1
            else:
                row += 1
        return False




