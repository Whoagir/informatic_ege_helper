from itertools import permutations

a = 'КОМПЬЮТЕР'
c = 0
a1 = sorted(a)
comb = permutations(a, r=9)
for i in comb:
    s = ''.join(i)
    if s[-2] == 'Е' and list(s[:4]) == sorted(list(s[:4])):
        c += 1
print(c)
