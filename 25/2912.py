
def all_divisors(n):
    dev = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            dev.append(i)
            dev.append(n // i)
            if len(dev)>6:
                break
    return sorted(list(set(dev)))


ans=[]
for n in range(157898, 157991):
    t=all_divisors(n)
    if len(t)==6:
        print(n,sorted(t))