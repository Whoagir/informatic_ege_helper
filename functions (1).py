def ctb(n:int,b:int)->str:
    r=''
    while n>0:
        d=str(n%b)
        r=d+r
        n//=b
    return r
def pr(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

def all_divisors(n):
    dev = []
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            dev.append(i)
            dev.append(n // i)
    return sorted(list(set(dev)))
