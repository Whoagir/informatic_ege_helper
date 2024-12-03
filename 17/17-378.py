# Автор: Е. Джобс

s = [int(x) for x in open('17_9372.txt')]
mx1001 = max(abs(x) for x in s if x % 1001 == 0)

p = []
for a, b in zip(s, s[1:]):
    if (100 <= abs(a) <= 999) or (100 <= abs(b) <= 999):
        if a + b > mx1001:
            p.append(a+b)

print(len(p), min(p))


