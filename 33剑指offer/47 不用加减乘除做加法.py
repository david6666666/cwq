'''
将两个数的加法看作两步，第一步是两个数相加但是不进位，第二步是记录之前的两数相加应该进位的地方加
上前一个相加但是不进位的数。对于具体的两个不小于0的数m和n，第一步可以看做m和n的异或运算m^n，第二步
可以看做m和n的与运算然后左移一位得到实际的进位位置(m&n)<<1。然后把两个得到的数字加起来继续操作，
指到carry进位为0终止操作。
'''
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF
        return num1 if num1 >> 31 == 0 else num1 - 4294967296