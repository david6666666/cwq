'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
'''
注意到每个非零整数n和n-1进行按位与运算，整数n的二进制数中最右边的1就会变成0，
那么二进制数中的1的个数就会减少一个，因此可以利用一个循环，使得 n = n&(n-1)
，计算经过几次运算减少到0，就是有几个1。注意：书中给了另外两种方法，分别是原
始n左移一位和右移一位的方法，因为Python不会出现整数溢出的情况，这里就不再考虑
着两种方法。扩展：判断一个数值是不是2得整数次方，如果是的话，这个数的二进制数中
有且只有一个1，那么这个数n会有 n&(n-1) == 0。或者求两个整数m和n需要改变m二进制
中的多少位才能得到n，可以先做 m^n 的异或运算，然后求这个数中有多少个1。
'''
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 0
        if base == 0:
            return False
        if exponent == 0:
            return 1
        if exponent <0:
            flag = 1
        result = 1
        for i in range(abs(exponent)):
            result *= base
        if flag == 1:
            result = 1/ result
        return result