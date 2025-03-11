def pr(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def all_divisors(n):
    dev = []
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            dev.append(i)
            dev.append(n // i)
    return sorted(list(set(dev)))


ans1 = []
ans2 = []
for n in range(25317, 51238):
    c,f=0,0
    p,j=0,0
    t = all_divisors(n)
    for i in range(len(t)):
        if pr(t[i]):
            c += 1
            if c >= 6:
                f = 1
                p=t[i]
                j=n
    if f == 1:
        ans1.append(p)
        ans2.append(j)
print(ans1, ans2)
