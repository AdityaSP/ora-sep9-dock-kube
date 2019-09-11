import bank
ac1 = bank.Account('Aditya')
print(ac1.n, ac1.b)
ac1.debit(100)
print(ac1.n, ac1.b)
ac1.credit(1000000)
print(ac1.n, ac1.b)
