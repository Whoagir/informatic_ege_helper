from sys import setrecursionlimit


def f(n):
    if n>=10000:
        return 1
    if n<10000 and n%2==0:
        return f(n+3)+7
    if n<10000 and n%2!=0:
        return f(n+1)-3
setrecursionlimit(10000)

print(f(50)-f(57))