def quickSort(arr,start,end):
    if start >= end:
        return
    low = start
    high = end
    basic_data = arr[start]
    while low < high:
        while low < high and arr[high] >= basic_data:
            high -= 1
        if arr[high] < basic_data:
            arr[low] = arr[high]
            low += 1
        while low < high and arr[low] < basic_data:
            low += 1
        if arr[low] > basic_data:
            arr[high] = arr[low]
            high -= 1
    arr[low] = basic_data

    quickSort(arr,start,low-1)
    quickSort(arr,high+1,end)


if __name__ == '__main__':
    list = [2,5,3,1,10,4]
    quickSort(list,0,len(list)-1)
    print(list)
    print('时间复杂度最好O（nlog2(n)），最差为O（n^2）')