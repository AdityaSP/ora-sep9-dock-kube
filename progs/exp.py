import sys
def f(n):
    li=[1,2]
    li[n]   
    1/n
    x    


try:    
    f(3) # index out of range
except IndexError as err:
    print(err)
try:
    f(0) # zero division error
except ZeroDivisionError as err:
    print(err)
try:    
    f(1) # name error
except NameError as err:
    print(err)


try:
    f(int(sys.argv[1]))
except NameError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
except IndexError as err:
    print(err)
except Exception as err:
    print(err)
    
print("End of Program")    
    


