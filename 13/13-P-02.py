from ipaddress import *
net = ip_network("162.198.0.44/255.255.255.240",0)
k = 0
for ip in net.hosts():
    k +=1
    if ip == ip_address("162.198.0.44"):
        print(k)
        break
    

    