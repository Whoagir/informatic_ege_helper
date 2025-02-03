f=[1]
for n in range(1,6*8**9):
    if n%2!=0:
        f.append(f[n//8]*(n%8))
    else:
        f.append(f[n//8])
    print(n)
c=0
for n in range(8**9,6*8**9+1):
    if f[n]==35:
        c+=1
print(c)