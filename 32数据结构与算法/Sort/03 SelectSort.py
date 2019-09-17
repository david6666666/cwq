def selectSort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i,n):
            if arr[min] > arr[j]:
                min = j
        if (i!=min):
            arr[i], arr[min] = arr[min], arr[i]
    return arr

a = [9,1,5,8,3,7,4,6,2]
b = selectSort(a)
print(b)

print('时间复杂度为O（n^2）')