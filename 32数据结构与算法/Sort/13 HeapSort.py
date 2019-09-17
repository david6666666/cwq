def heapify(tree, n, i):#i为第i个节点
    if (i >= n):
        return tree
    c1 = 2*i+1  #左子节点
    c2 = 2*i+2  #右子节点
    max = i
    if (c1 < n and tree[c1] > tree[max] ) :
        max = c1
    if (c2 < n and tree[c2] > tree[max] ) :
        max = c2
    if (max != i):
        tree[max], tree[i] = tree[i], tree[max]
        heapify(tree,n,max)

def build_heap(tree, n):
    last_node = n-1
    #最后一个非叶子节点
    parent = (last_node-1) // 2
    for i in range (0,parent+1)[::-1]:
        heapify(tree,n,i)

def heap_sort(tree,n):
    build_heap(tree,n)
    print(tree)
    for i in range(0,n)[::-1]:
        tree[0],tree[i] = tree[i],tree[0]
        heapify(tree,i,0)

if __name__ == '__main__':
    tree = [2,5,3,1,10,4]
    heap_sort(tree,len(tree))
    print(tree)
    print('时间复杂度O（nlog2(n)）')

