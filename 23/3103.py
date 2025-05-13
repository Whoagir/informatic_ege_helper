def f(x,y):
    if x>y:
        return 0
    if x==y:
        return 1
    else:
        if str(x)[-1]=='9':
            return f(x + 1, y) + f(x + 10, y)
        else:
            return f(x + 1, y) + f(x + 11, y)
print(f(26,49))