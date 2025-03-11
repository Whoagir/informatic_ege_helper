from sys import setrecursionlimit


def f(n):
    if n==1:
        return 1
    if n>1:
        return n+f(n-1)
c=0
setrecursionlimit(2300)
for n in range(1,101):
    if (f(2023)//f(n))%2==0:
        c+=1
print(c)