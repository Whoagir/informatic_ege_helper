def ctb(n: int, b: int) -> str:
    r = ''
    while n > 0:
        d = str(n % b)
        r = d + r
        n //= b
    return r


s = 86
for b in range(2, 16):
    r = ctb(s, b)
    print(r, b)
