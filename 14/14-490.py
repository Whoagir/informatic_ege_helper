# Автор: К. Багдасарян

def f( n ):
    cnt5 = cnt3 = 0
    while n != 0:
        if n%6 == 3:
            cnt3 += 1
        if n%6 == 5:
            cnt5 += 1
        n //= 6
    return (cnt3 == cnt5)


for x in range(10000,0,-1):
    n = 6**900 + 6**10 - x
    if f( n ):
        print(x)
        break

