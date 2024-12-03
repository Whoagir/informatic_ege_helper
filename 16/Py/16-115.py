def F( n ):
  return 1 if n <= 1 else \
         2*F(n-1) + F(n-2) if n > 1 and n % 3 == 0 else \
         3*F(n-2) + F(n-1);

def isPrime( n ):
  return all(
         n % d != 0
         for d in range(2,int(n**0.5)+1)
         )

count = 0
for i in range(2,35+1):
  if isPrime( sum(map(int, str(F(i)))) ):
    count += 1

print( count )