import time
import random

def timer(f):
	def wrapper():
		s = time.time()
		f()
		e = time.time()
		print("Took", e-s , "seconds")
	return wrapper
    
@timer
def heavyduty():
	time.sleep(random.randint(1,5))
    
    
heavyduty()    