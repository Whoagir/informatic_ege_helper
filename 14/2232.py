def ctb(n: int, b: int) -> str:
    r = ''
    while n > 0:
        d = str(n % b)
        r = d + r
        n //= b
    return r


mn = 0
s = 9 ** 7 + 3 ** 8 - 5
s1 = ctb(s, 3)
print(s1)
# a=s1.count('0')
# k=s1.count('1')
# l=s1.count('2')
# if a<n:
#     a