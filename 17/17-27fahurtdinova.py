# Автор: А.А. Фахуртдинова

n, k = 8432, 3712
s = [13, 14, 15]
ns = [n // i * i for i in s]  # Максимальные числа, из диапазона, делящиеся на заданные делители
a = set()
for i in range(len(s)):  # Генерация множества чисел
    a |= set( x for x in range(ns[i], k-1, -s[i])
                if (x % 2 == x % 4) )
print( len(a), min(a) )

# Другой вариант

s = 8432
d = [13, 14, 15]
s13, s14, s15, e = s // 13 * 13, s // 14 * 14, s // 15 * 15, 3712
a  = set( x for x in range(s13, e-1, -13) if (x % 2 == x % 4) )
a |= set( x for x in range(s14, e-1, -14) if (x % 2 == x % 4) )
a |= set( x for x in range(s15, e-1, -15) if (x % 2 == x % 4) )
print(len(a), min(a))
