class Account():
    def __init__(self, n, b=1000, t='S'):
        self.n = n
        self.b = b
        self.t = t
    def credit(self, amount):
        self.b += amount
    def debit(self, amount):
        self.b -= amount
        
        