def r(n):
    n_bi = bin(n)[2:]
    for _ in range(2):
        c1 = n_bi.count('1')
        if c1 % 2:
            n_bi = '1' + n_bi + '00'
        else:
            n_bi = n_bi[1:].lstrip('0')
    return int(n_bi, 2)


n = 1
while r(n) <= 100:
    n += 1
print(n)
