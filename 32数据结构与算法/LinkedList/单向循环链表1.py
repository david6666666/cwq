class SingleNode(object):
    """单链表的节点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点
        self.next = None

class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self,node=None):
        self.__head = node
        if node:
            node.next = node


    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while(cur.next != self.__head):
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur.next != self.__head :
            print(cur.item,end=' ')
            cur = cur.next
        print(cur.item,end=' ')

    def add(self,item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            #退出循环，cur指向为节点
            node.next = self.__head
            self.__head = node
            cur.next = self.__head
    def append(self,item):
        """尾部添加元素"""
        node =SingleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while(cur.next != self.__head):
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self,pos,item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self,item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    #找尾节点
                    rear = self.__head
                    while rear.next!= self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.item == item:
            if cur == self.__head:
                #链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False

if __name__ == "__main__":
    ll = SingleCycleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())

    ll.travel()
    print(ll.search(3))

    print(ll.search(7))

    ll.remove(6)
    print("length:", ll.length())

    ll.travel()