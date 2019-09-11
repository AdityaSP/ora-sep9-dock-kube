def add(x,y):
    return x*x + y*y
def sub(x,y):
    return x - y



#print(__name__)

if __name__ == '__main__':
    import sys
    print(sys.argv)
    print(add( int(sys.argv[1]) , int(sys.argv[2]) ))
