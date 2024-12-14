# Автор: Е. Джобс

def f(a, b, m):
    if a >= 50 or b >= 50:
        return m % 2 == 0
    if m == 0:
        return False
    h = (f(x, y, m-1)
         for x, y in ((a+3, b), (a*2, b), (a, b+3), (a, b*2)))
    return all(h) if m % 2 == 0 else any(h)

print( "19)", [S for S in range(1, 28) if f(22, S, 2)])
print( "20)", [S for S in range(1, 28) if f(22, S, 3) and not f(22, S, 1)])
print( "21)", [S for S in range(1, 28) if f(22, S, 4) and not f(22, S, 2)])




