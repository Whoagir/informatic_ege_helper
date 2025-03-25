from sys import setrecursionlimit


def f(n):
    if n>3456:
        return n+1
    if n<=3456 and n%3==0:
        return f(n+1)+f(n+2)
    if n<=3456 and n%3!=0:
        return f(n+n%3)+2
setrecursionlimit(10000)
print(f(12)-f(17))
