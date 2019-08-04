import threading
import time

class MyThread1(threading.Thread):
    def run(self):
       if mutexA.acquire():
           print('thread1 do something...')
           time.sleep(2)
           if mutexB.acquire():
               print('thread1 get mutexB')
               mutexB.release()
           mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
       if mutexB.acquire():
           print('thread2 do something...')
           time.sleep(2)
           if mutexA.acquire():
               print('thread2 get mutexB')
               mutexA.release()
           mutexB.release()

if __name__ == '__main__':
    mutexA=threading.Lock()
    mutexB=threading.Lock()
    t1=MyThread1()
    t1.start()

    t2=MyThread2()
    t2.start()
