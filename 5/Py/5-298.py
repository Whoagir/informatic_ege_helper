# Автор В.Н. Шубинкин

def r(n):
    n_bi = bin(n)[2:]
    for _ in range(2):
        c1 = n_bi.count('1')
        if c1 % 2:
            n_bi = '1'*(c1 + 1)
        else:
            n_bi = n_bi[1:]
    return int(n_bi, 2)

c = 0
for n in range(1, 1001):
    c += r(n) == 7
print(c)
