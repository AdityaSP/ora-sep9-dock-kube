ui = input("Enter , seperated string of integers:" ).strip().split(',')
#1,2,3 ---> ['1', '2', '3']
total = 0
for i in ui:
    total += int(i)
print("The summation is", total)
    
