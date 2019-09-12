# -*- coding:UTF-8 -*-
'''
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
'''
# 基于循环求点数, 时间性能好。用两个数组来存储骰子点数的每一个总数出现次数。在一次循环中，第一个数
# 组中的第n个数字表示骰子和为n出现的次数。在下一次循环中加入一个新的骰子，此时和为n的骰子出现的次
# 数应该等于上一次循环中骰子点数和为n-1，n-2，n-3，n-4，n-5，n-6的次数的总和，也就是把另一个数组
# 的第n个数字对应上一个数组的n-1，n-2，n-3，n-4，n-5，n-6的次数的总和。同时需要注意的是，每次使
# 用新数组的时候，需要把数组所有位置清零，因为我们对于第n位进行的累加操作，如果之前第n位有数字但
# 不清零的话，会导致结果偏大。
def PrintProbability(number):
    if number < 1:
        return
    maxVal = 6
    # 构造两个数组来存储骰子点数的每一个总数出现的次数

    probStorage = [[], []]
    probStorage[0] = [0]*(maxVal * number + 1)
    flag = 0
    # 在一次循环中, 第一个数组中的第n个数字表示骰子和为n出现的次数
    for i in range(1, maxVal+1):
        probStorage[flag][i] = 1
    # 在下次循环中, 另一个数组的第n个数字设为前一个数组对应的第n-1、n-2、n-3、n-4、n-5、n-6之和
    for time in range(2, number+1):
        probStorage[1-flag] = [0]*(maxVal * number + 1)
        for pCur in range(time, maxVal*time+1):
            diceNum = 1
            while diceNum < pCur and diceNum <= maxVal:
                probStorage[1-flag][pCur] += probStorage[flag][pCur-diceNum]
                diceNum += 1
        flag = 1 - flag


    total = maxVal ** number
    for i in range(number, maxVal*number+1):
        ratio = probStorage[flag][i] / float(total)
        print("{}: {:e}".format(i, ratio))
s = PrintProbability(5)