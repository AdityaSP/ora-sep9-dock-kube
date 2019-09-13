from threading import Thread, Lock
import time

count = 0
l = Lock()

def counter():
    global count
    time.sleep(1)
    l.acquire()
    a = count
    time.sleep(1)
    a = a+1
    count = a
    print(count)
    l.release()
    time.sleep(1)
    
for i in range(5):
    Thread(target=counter).start()