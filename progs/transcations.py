import bank
sa = bank.SA('Aditya')
print(sa.n, sa.b)
sa.credit(100)
sa.debit(2000)
print(sa.n, sa.b)

ca = bank.CA('ABC Inc.')
print(ca.n, ca.b)
ca.credit(100)
ca.debit(2000)
print(ca.n, ca.b)






#ac1 = bank.Account('Aditya')
#print(ac1.n, ac1.b)
#ac1.debit(100)
#print(ac1.n, ac1.b)
#ac1.credit(1000000)
#print(ac1.n, ac1.b)
