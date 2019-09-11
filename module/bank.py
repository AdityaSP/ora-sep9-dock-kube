class InsufficientBalanceError(Exception):
    pass

class Account():
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t
    def credit(self, amount):
        self.b += amount
    def debit(self, amount):
        self.b -= amount

class SA(Account):
    def __init__(self, n, b=1000):
        Account.__init__(self, n, b, 'S')
    def debit(self, amount):
        if self.b < amount:
            raise InsufficientBalanceError('Not enough money')
        else:
            Account.debit(self, amount)

class CA(Account):
    def __init__(self, n, b=0):
        Account.__init__(self, n, b, 'C')
        
        