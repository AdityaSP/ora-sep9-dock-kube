ip = input("Enter an ip address: ")
#print(ip)
#124.56.78.98

ip_li = ip.split('.')
ip_li[-1] = str(int(ip_li[-1])+1)
print("Next IP is", '.'.join(ip_li))

