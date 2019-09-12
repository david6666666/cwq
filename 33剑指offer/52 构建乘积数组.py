# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if A == None or len(A) <= 0:
            return
        length = len(A)
        C = [1] * length
        for i in range(1, length):
            C[i] = C[i-1] * A[i-1]
        temp = 1
        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            C[i] *= temp
        return C

test = [1, 2, 3, 4]
s = Solution()
print(s.multiply(test))