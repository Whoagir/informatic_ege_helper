# Автор: Н. Сафронов

def three(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


a = []
for N in range(11, 50):
    r = three(N)
    print( N, r, end=" ")
    cht = len([x for x in r if x in '02'])
    cn = r.count('1')
    if cht > cn:
        r = '22' + r
    else:
        r = '11' + r
    print( r, end=" ")
    r = int(r, 3)
    print( r)
    if r > 100:
        a.append(r)

print(min(a))
