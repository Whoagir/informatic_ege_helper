# Автор: К. Багдасарян

def f( n ):
    cnt1 = 0
    while n != 0:
        if n%9 == 1:
            cnt1 += 1
        n //= 9
    return cnt1

mx = -float('inf')
for x in range(1, 2001):
    n = 9**250 + 9**150 - x
    r = f( n )
    if r >= mx:
        mx = r
        ans = x
print(ans)


