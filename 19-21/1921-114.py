# Автор: Д. Статный

def f(s, m):
    if s>=100: return m%2!=0
    if m==0: return 0
    h = [f(s*2, m-1), f(s+2, m-1), f(s+4, m-1)]
    return any(h) if m%2!=0 else all(h)

print('19)', [s for s in range(1, 100) if f(s, 3) and 1-f(s, 1)])
print('20)', [s for s in range(1, 100) if f(s, 6) and 1-f(s, 4) and 1-f(s, 2)])
print('21)', [s for s in range(1, 100) if f(s, 5) and 1-f(s, 3) and 1-f(s, 1)])

