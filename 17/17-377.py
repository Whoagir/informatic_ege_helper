# Автор: Е. Джобс

s = [int(x) for x in open('17.txt')]
m17 = max(x for x in s if x % 17 == 0)

p = []
for a, b in zip(s, s[1:]):
    if (a+b) > m17:
        p.append(a+b)
print(len(p), max(p))

