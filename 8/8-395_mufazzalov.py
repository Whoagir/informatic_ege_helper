# Муфаззалов Д.Ф.
def f(n):
    p = n
    for j in range(2, n):
        p *= j
    return p


a = list('негнипапинген')
b = [i for i in set(a) if a.count(i) % 2 == 0 for j in range(a.count(i) // 2)]

ans = f(len(b))
for j in set(b):
    ans //= f(b.count(j))
print(ans)
# -------------------------------------------------------------


from itertools import permutations as p

a = list('негнипапинген')
b = [i for i in set(a) if a.count(i) % 2 == 0 for j in range(a.count(i) // 2)]
print(len(set(p(b))))
