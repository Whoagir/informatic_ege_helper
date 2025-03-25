k=0
for a in range(1,1000):
    c=0
    for x in range(1,1001):
        f=(a%35==0) and ((730%x==0)<=((not(a%x==0))<=(not 110%x==0)))
        if f:
            c+=1
        if c==1000:
            k+=1
print(k)