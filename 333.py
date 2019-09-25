def bubbleSort(arr):
    flag = 1
    n = len(arr)
    for i in range(n - 1):
        if flag:
            flag = 0
            for j in range(n - 1 - i):
                if arr[j][1] > arr[j + 1][1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = 1
        else:
            break
    return arr

ss = input().split(' ')
sss = []
res = []
for i in range(len(ss)):
    sss.append(ss[i].split('：'))

ssss = bubbleSort(sss)
for i in range(len(ssss)):
   res.append('：'.join(ssss[i]))
print(' '.join(res))
