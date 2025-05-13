from sys import setrecursionlimit


c=0
F=[0]
for n in range(1,567654321):
    F.append(F[n-1]+5*n)
    if n>=189456678 and F[n]%7!=0:
        c+=1
print(c)