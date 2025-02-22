c=0
for n in range(1,1000):
    if n%2==0:
        n1=n/2
    else:
        n1=n-1
    if n1%3==0:
        n2=n1/3
    else:
        n2=n1-1
    if n2%5==0:
        n3=n2/5
    else:
        n3=n2-1
    if n3==3:
        c+=1
print(c)