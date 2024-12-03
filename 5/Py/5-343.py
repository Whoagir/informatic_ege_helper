# Автор: Н. Сафронов

def three(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


a = []
for n in range(1, 50):
    r = three(n)
    if sum(map(int, r)) % 3 == 0:
        r = '20' + r
    else:
        r = '10' + r
    r = int(r, 3)
    if r < 100:
        a.append(n)
print(max(a))
