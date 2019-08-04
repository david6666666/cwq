def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr,right_arr)
def merge(left_arr,right_arr):
    l_index = 0
    r_index = 0
    merge_arr = []
    while l_index < len(left_arr) and r_index < len(right_arr):
        if left_arr[l_index] <= right_arr[r_index]:
            merge_arr.append(left_arr[l_index])
            l_index += 1
        else:
            merge_arr.append(right_arr[r_index])
            r_index += 1
    # 当其中一个列表的指针到头是 将另一个加进去
    merge_arr += left_arr[l_index:]
    merge_arr += right_arr[r_index:]
    return merge_arr

if __name__ == '__main__':
    list = [28,32,14,12,51,42]
    a = merge_sort(list)
    print(list)
    print(a)
    print('时间复杂度为O（nlog2(n)）')