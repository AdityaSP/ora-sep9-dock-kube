import time
from threading import Thread

def somework(x):
    print("started", x)
    time.sleep(3)
    print("done", x)
    
    
#for i in range(5):
#    somework(i)  #sync


for i in range(5):
    t = Thread(target=somework, args=(i,))
    t.start()  #async
    
    
