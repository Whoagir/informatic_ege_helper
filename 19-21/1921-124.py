# Автор: Е. Джобс

def g(a, b, m):
    if a*b >= 123:
        return m % 2 == 0
    if m == 0:
        return False
    h = (g(a+2, b, m-1), g(a*2, b, m-1), g(a, b+2, m-1), g(a, b*2, m-1))
    if m % 2 == 0:
        return all(h)
    else:
        return any(h)

print( "20)", [S for S in range(1, 41) if not g(3, S, 1) and g(3, S, 3)])
print( "21)", [S for S in range(1, 41) if not g(3, S, 2) and g(3, S, 4)])




