'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩
阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字
1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
'''
首先需要判断每一步开始是的坐标点是否满足小于行数的一半且小于列数的一半，在最后一
圈中，可能出现仅能向右走一行，仅能向右走一行向下走一列，向右走一行向下走一列向左
走一行，能走完整一圈，一共四种情况。其中只有能向右走一行必然发生，不必判断，剩余
的都需要判断发生条件。
'''
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix == None:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        result = []
        while rows > start*2 and cols >start*2:
            endX = cols - 1 - start
            endY = rows - 1 - start
            #从左到右打印一行
            for i in range(start,endX+1):
                result.append(matrix[start][i])
            #从上到下打印一列
            if start < endY:
                for i in range(start+1,endY+1):
                    result.append(matrix[i][endX])
            #从右到左打印一行
            if start < endX and start < endY:
                for i in range(endX-1,start-1,-1):
                    result.append(matrix[endY][i])
            if start < endX and start < endY -1:
                for i in range(endY-1,start,-1):
                    result.append(matrix[i][start])
            start+=1
        return result