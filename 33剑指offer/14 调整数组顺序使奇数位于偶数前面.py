'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
'''
注重函数的扩展性能。把函数中的判断条件写成一个判断条件的函数，方便与函数的扩展。
对于奇数位于偶数前面的情况，类似于快排，在头和尾分别设置一个指针，头指针指向奇数则后
移，尾指针指向偶数则前移。
'''

class Solution:
    # 一个类似于快排的方法, 只是简单的满足了奇数在前,偶数在后, 奇数的顺序发生了改变
    def reOrderArray(self, array):
        if len(array) <1:
            return
        elif len(array) == 1:
            return array
        front = 0
        rear = len(array)-1
        while front <rear:
            while array[front] % 2 == 1:
                front +=1
            while array[rear] % 2 == 0:
                rear -=1
            array[front],array[rear] = array[rear],array[front]
            front +=1
            rear -=1
        return array

S = Solution()
print(S.reOrderArray([1,2,4,3,5]))
