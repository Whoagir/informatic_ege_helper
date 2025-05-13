def f(x,y,c):
    if x>y or c>2:
        return 0
    if x==y:
        return 1
    else:
        if x%2==0:
            return f(x + 2, y,c+1) + f(x * 2, y,c+1) + f(x * 3, y,c+1)
        else:
            return f(x + 2, y,c) + f(x * 2, y,c) + f(x * 3, y,c)
print(f(1,402,0))