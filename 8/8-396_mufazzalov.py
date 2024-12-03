import collections
from math import factorial as f

s = 'Лёша на полке клопа нашёл.'
a = [i.lower() for i in s if i.isalpha()]
c = collections.Counter(a)
b = [i for i in set(a) for _ in range(c[i] // 2)]
ans = f(len(b))
for j in set(b):
    ans //= f(c[j] // 2)
print(ans)
