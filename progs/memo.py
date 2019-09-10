import time

def memo(f):
    d = {}
    def wrapper(x):
        if x not in d:
            d[x] = f(x)
        return d[x]
    return wrapper    

@memo
def calc(x):
    time.sleep(5)
    return x ** 4
    
    
print(calc(4))
print(calc(4))
print(calc(4))
print(calc(5))
print(calc(5))
print(calc(5))
print(calc(5))
print(calc(4))






