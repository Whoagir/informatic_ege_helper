from sys import setrecursionlimit


def f(n):
    if n==1:
        return 2
    else:
        return f(n-1)*(3**(n%5))/(3**(n%7))
setrecursionlimit(2000)
for n in range (1,30):
    print(f(n))
s=f(1025)
s1=f(1030)
print(s,s1)
print(s/s1)