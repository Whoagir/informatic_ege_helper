def ctb(n: int, b: int) -> str:
    r = ''
    while n > 0:
        d = str(n % b)
        r = d + r
        n //= b
    return r


s = 49 ** 129 + 7 ** 131 - 2
s1 = ctb(s, 7)
# print(s1)
v = s1.replace('0', '6')
# print(v)
res = v.count('6')
print(res)