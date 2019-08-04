def bubbleSort2(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

def bubbleSort3(arr):
    flag = 1
    n = len(arr)
    for i in range(n - 1):
        if flag:
            flag = 0
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = 1
            print(arr)
        else:
            break
    return arr

a = [11, 5, 6, 1,9]
b = [1,2,3,5,7,6]
c = bubbleSort2(a)
print(c)
print('------------')
d = bubbleSort3(b)
print(d)

print('时间复杂度最好O（n），最差为O（n^2）')