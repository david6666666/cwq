'''
先入先出队列 Queue
后入先出队列 LifoQueue
优先级队列 PriorityQueue
'''
import threading
import time
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while   True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count +1
                    msg = '生产产品' +str(count)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = Queue()
    for i in range(500):
        queue.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()