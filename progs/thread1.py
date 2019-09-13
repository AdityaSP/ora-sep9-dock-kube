import time
from threading import Thread
import threading

def somework(x):
    print(threading.current_thread().name)
    print("started", x)
    time.sleep(3)
    print("done", x)
    
    
#for i in range(5):
#    somework(i)  #sync
somework(100)

for i in range(5):
    t = Thread(target=somework, name='Thread-' + str(i), args=(i,))
    t.start()  #async
    
    
