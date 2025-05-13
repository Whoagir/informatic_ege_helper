from sys import setrecursionlimit

setrecursionlimit(200)
def f(x,y):
    if x<y:
        return 0
    if x==y:
        return 1
    else:
        if x>4:
            return f(x-1,y)+f(x-3,y)+f(x%4,y)
        else:
            return f(x-1,y)+f(x-3,y)
print(f(22,2))