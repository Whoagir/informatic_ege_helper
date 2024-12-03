# Авторы: Д. Статный, М. Шагитов

from functools import cache

@cache
def f(l, c, k2):
    k2 += c=='Ч'
    if l==8: return k2==3
    return sum(f(l+1, i, k2) for i in 'Ч'*8+'Н'*8)

print(sum(f(1, i, 0) for i in 'Ч'*7+'Н'*8))
