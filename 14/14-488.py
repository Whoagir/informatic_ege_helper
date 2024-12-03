# Автор: К. Багдасарян

def f( n ):
    cnt4 = 0
    while n != 0:
        if n%5 == 4:
            cnt4 += 1
        n //= 5
    return cnt4

mx = -float('inf')
for x in range(2, 2026):
    n = 5**2025 + 5**200 - x
    r = f( n )
    if r >= mx:
        mx = r
        ans = x
print( ans )
