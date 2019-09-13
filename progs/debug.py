import pdb
pdb.set_trace()

def f1(arg):
    arg = arg + 1
    return arg
def f2(arg):
    arg = arg + 1
    return arg

def f3(arg):
    arg = arg + 1
    return arg
    
print("Here")
print(f1(f2(f3(3))))
    
        