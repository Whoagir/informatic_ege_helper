from functions import ctb
c=0
for i in range(2,11):
    s=ctb(188,i)
    d=[int(j) for j in s]
    if d==sorted(d):
        print(i,s)
print(c)