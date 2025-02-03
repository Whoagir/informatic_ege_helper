from sys import setrecursionlimit


def f(n):
    if n>=10000:
        return n
    if n<10000 and n%4==0:
        return n/4+f(n/4+2)
    if n<10000 and n%4!=0:
        return 1+f(n+2)
setrecursionlimit(10000)
print(f(174)-f(3))