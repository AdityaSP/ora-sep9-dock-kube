from threading import Thread, Event
import time

pe = Event()    
ce = Event()    
    
a = 0

def consumer():
    for i in range(5):
        time.sleep(3)
        pe.wait()
        print(a)
        pe.clear()
        ce.set()
    
def producer():
    global a
    for i in range(5):
        time.sleep(5)        
        a = a + 100
        pe.set()
        ce.wait()
        ce.clear()


pt = Thread(target=producer)
ct = Thread(target=consumer)

pt.start()
ct.start()

        