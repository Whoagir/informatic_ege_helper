for n in range(500, 5000):
    s = bin(n)[2:]
    s1 = s[::-1]
    s1 = str(int(s1))
    r = int(s1, 2)
    if r == 19:
        print(n, r)
