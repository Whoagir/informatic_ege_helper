
def F( n ):
  return 0 if n < 10 else \
         F(n//10) + (n//10%10) - n%10

# исследование частных случаев
for n in range(1, 1000):
  if (f := F(n)) == 9:
    print( n, f )

# вывод: F(n) == 9 для n, которые начинаются с 9 и заканчиваются на 0
count = sum( 10**(k-2) for k in range(2,11) )
print( count )

