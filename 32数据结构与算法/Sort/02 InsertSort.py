def insertSort(arr):
    for index in range(1,len(arr)):
        while index>0 and arr[index-1] > arr[index] :
            arr[index-1], arr[index] = arr[index], arr[index-1]
            index -= 1
        print(arr)
    return arr

a = [11, 5, 6, 1,9]
b = insertSort(a)
print(b)

print('时间复杂度最好O（n），最差为O（n^2）')