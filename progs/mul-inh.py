class A():
    def f1(self):
        print("from A")
        
class B(A):
#    pass
    def f1(self):
        print("from B")

class C(A):
#    pass
    def f1(self):
        print("from C")
        
        
class D(C,B):   
    pass

#linearlization of multi derived classes
#mro -> method resolution order
print(D.mro())
    
objd = D()
objd.f1()

    