# Авторы: Д. Статный, М. Шагитов

from functools import cache

@cache
def f(p, k2, k3, l):
    k2 += p=='2'
    k3 += p=='3'
    if l==10: return k2==k3
    return sum(f(i, k2, k3, l+1) for i in '0123456789')
print(sum(f(i, 0, 0, 1) for i in '123456789'))

