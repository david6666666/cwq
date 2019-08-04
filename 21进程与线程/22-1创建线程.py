import threading
import time

def fun(num):
    print("线程执行%d"%num)
    time.sleep(2)

for i in range(5):
    t = threading.Thread(target=fun, args=(i+1,))
    t.start()

print("主线程结束")