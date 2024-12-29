def F(n):
    global e
    e = n
    if n > 0:
        d = n % 10 + F(n // 10)
        e = d
        return d
    else:
        return 0


for n in range(1, 10000):
    e=0
    F(n)
    if e>32:
        print(n,F(n))
        break