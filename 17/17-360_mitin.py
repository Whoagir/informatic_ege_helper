# Автор: И. Митин

def p(n):
    s = 1
    for i in str(n):
        s *= int(i)
    return s


def c(a,b,c):
    ab = (a == -b)
    bc = (b == -c)
    ac = (a == -c)
    return ab or bc or ac


def s(a,b,c):
    mn = 10**20
    ab = (a == -b)
    bc = (b == -c)
    ac = (a == -c)
    if ab:
        mn = min(a**2,mn)
    if bc:
        mn = min(b**2,mn)
    if ac:
        mn = min(a**2,mn)
    return mn


a = [int(x) for x in open("17-360.txt")]
mx = max(i for i in a if p(abs(i))%100==42)
ans = []
for i in range(len(a)-2):
    if c(a[i],a[i+1],a[i+2]) and a[i] < mx and a[i+1] < mx and a[i+2] < mx:
        ans.append(s(a[i],a[i+1],a[i+2]))
print(len(ans), min(ans))
