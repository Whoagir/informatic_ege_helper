counter = 0
a = set()
for n in range(1,1000):
    s = bin(n)[2:]
    b = s.count('1')
    if b > s.count('0'):
        s1 = s + str(b % 2) + '0'
    else:
        s1 = s + str(b % 2) + '1'
    r = int(s1, 2)
    if 50<=r<=80:
        a.add(r)
print(len(a))
