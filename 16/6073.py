c=0
f=[0]
for n in range(1,213789654):
    f.append(f[n-1]+3*n)
    if n>=123456789 and f[n]%5!=0:
        c+=1
print(c)