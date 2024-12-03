# Авторы: Д. Статный, М. Шагитов

from functools import cache

@cache
def f(l, c, k, s):
    k += c=='A'
    s = ''.join(set(s))
    if l==8: return k<=2 and len(s)==6
    return sum(f(l+1, i, k, s+i) for i in '0123456789ABC')
print(sum(f(1, i, 0, i) for i in '123456789ABC'))

