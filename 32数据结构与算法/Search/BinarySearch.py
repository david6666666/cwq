def binarySearch(list,key):
    n = len(list)
    low = 0
    high = n - 1
    while(low <= high):
        mid = (low +high)//2
        if key>list[mid]:
            low = mid+1
        elif key<list[mid]:
            high = mid -1
        else:
            return mid
    return False

if __name__ == '__main__':
    a = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    print(binarySearch(a,123))