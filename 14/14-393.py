def toBase5( n ):
  return str(n) if n < 5 else \
         toBase5( n // 5 ) + str(n%5)

result = (0, 0)
for x in range(4,10):
  p = int( f"4{x}B5", 26 ) * int( f"2{x}3", x+1 )
  s5 = toBase5( p )
  sum5 = sum(map(int, s5))
  count4 = s5.count('4')
  if sum5 == 19:
    print( x, sum5, count4, p )
    if count4 > result[1]:
       result = ( x, count4, p )

print( result )


# Автор: И. Карпачев

def dec(arr, q):
    arr = arr[::-1]
    r = 0
    for i in range(len(arr)):
        r += arr[i] * q ** i
    return r

print('\nx       v       k')
for x in range(4, 10):
    v = dec([4, x, 11, 5], 26) * dec([2, x, 3], x+1)
    a = v
    s = 0 # сумма цифр в 5-ричной записи
    k = 0 # количество цифр 1 в 5-ричной записи
    while a != 0:
        if a % 5 == 4:
            k += 1
        s += a % 5
        a //= 5
    if s == 19:
        print(x, v, k)
