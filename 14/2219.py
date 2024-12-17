def ctb(n: int, b: int) -> str:
    r = ''
    while n > 0:
        d = str(n % b)
        r = d + r
        n //= b
    return r


s = 9 ** 22 + 3 ** 66 - 18
s1 = ctb(s, 3)
res = s1.count('2')
print(res)
