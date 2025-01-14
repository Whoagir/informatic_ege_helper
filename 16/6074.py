from sys import setrecursionlimit


def F(n):
    if n==0:
        return 0
    else:
        return F(n-1)+5*n
setrecursionlimit(1000)
c=0
for n in range(189456678,567654321):
    if F(n)%7!=0:
        c+=1
print(c)