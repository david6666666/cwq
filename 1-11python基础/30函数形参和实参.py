def printMax(a,b):      #形参
    '''用于比较两个数的大小，打印较大的值'''     #文档字符串
    if a>b:
        print(a,'较大值')
    else:
        print(b,'较大值')

printMax(10,20)         #实参
help(printMax.__doc__)

#文档字符串(函数的注释)