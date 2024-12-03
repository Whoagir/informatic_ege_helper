# Автор: Е. Джобс

s = [int(x) for x in open('17-382.txt')]
mn11 = min(x for x in s
           if (x % 100 == 11) and (100 <= x <= 999))

p = []
for a, b in zip(s, s[1:]):
# for i in range(1, range(len(s))):
#   a, b = s[i-1], s[i]
    if (not(100<=a<=999)) != (not(100<=b<=999)):
        if abs(a-b) % mn11 == 0:
            p.append(a+b)
print(len(p), max(p))

