def ctb(n: int, b: int) -> str:
    r = ''
    while n > 0:
        d = str(n % b)
        r = d + r
        n //= b
    return r


for n in range(1, 1000):
    s = ctb(n, 4)
    if n % 2 == 0:
        s1 = '13' + s + '02'
    else:
        s1 = '2' + s + '11'
    r = int(s1, 4)
    if r > 1000:
        print(r)
