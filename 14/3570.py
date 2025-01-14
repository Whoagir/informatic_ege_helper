from functions import ctb
for n in range(1,1000):
    a=hex(n)[2:]
    a1=oct(n)[2:]
    a2=ctb(n,4)
    a3=bin(n)[2:]
    if a[0]=='e':
        if a1[1]=='5':
            if a2[-1]=='1':
                if a3[5]=='1':
                    print(n)