def shellSort(arr):

    n = len(arr)
    gap = n // 2
    #gap变化到0之前，插入算法执行的次数
    while gap >= 1:
        #插入算法，与普通插入算法的区别就是gap步长
        for j in range(gap,n):
            i = j
            while i > 0:
                if arr[i-gap] >arr[i]:
                    arr[i-gap], arr[i] = arr[i], arr[i-gap]
                    i -= gap
                else:
                    break
        gap //= 2
    return arr
a = [9,1,5,8,3,7,4,6,2]
shellSort(a)
print(a)

print('时间复杂度最好O（nlog(n)），最差为O（n^2）,平均O（n^1.3）')