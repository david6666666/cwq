from multiprocessing import Process,Pool
import os,time,random

def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg,os.getpid()))
    time.sleep(2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop-t_start))

pool = Pool(3)
for i in range(10):
    pool.apply_async(worker, (i,))    #异步请求，使用非阻塞额的方式调用func

print('-----start-----')
pool.close()
pool.join()
print('-----end------')

