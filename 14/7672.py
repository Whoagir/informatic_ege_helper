def ctb(n: int, b: int) -> str:
    r = ''
    while n > 0:
        d = str(n % b)
        r = d + r
        n //= b
    return r


c = 0
for n in range(70000, 60001,-1):
    s = 5 ** 2025 + 5 ** 400 - n
    s1 = ctb(s, 5)
    v = s1.count('4')
    if v > c:
        c = v
        print(n)
