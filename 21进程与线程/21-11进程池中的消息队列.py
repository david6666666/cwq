from multiprocessing import Pool, Manager
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
        else:
            break
if __name__=='__main__':
    q = Manager().Queue()
    pool = Pool(3)
    pool.apply(write,(q,))
    pool.apply(read,(q,))
    pool.close()
    pool.join()
    print('所有数据已读完')