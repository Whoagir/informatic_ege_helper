from sys import setrecursionlimit


def F(n):
    if n==0:
        return 2
    if 0<n<=15:
        return F(n-1)
    if 15<n<95:
        return 1.6*F(n-3)
    if n>=95:
        return 3.3*F(n-2)
setrecursionlimit(1300)
print(F(33))