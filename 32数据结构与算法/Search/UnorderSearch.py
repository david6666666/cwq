def unorder_search(list,key):
    n = len(list)
    for i in range(n):
        if list[i] == key:
            return i
    return False

#设置一个哨兵，可以解决不需要每次让i与n做比较
def unorder_search_better(list,key):
    n = len(list)
    list.append(key)
    i = 0
    while(list[i] != key):
        i += 1
    list.pop()
    if i == n:
        return False
    else:
        return i

if __name__ == '__main__':
    a = [9,4,5,6,10,3]
    print(unorder_search_better(a,4))