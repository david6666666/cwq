from multiprocessing import Process,Pool
import os,time,random

def worker(msg):
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    t_start = time.time()
    time.sleep(2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop-t_start))

pool = Pool(3)

for i in range(10):
    pool.apply(worker, (i,))    #同步请求,使用阻塞方式调用func

print('-----start-----')
pool.close()    #关闭Pool，使其不在接受新的任务
pool.join()
print('-----end------')

