def F( n ):
  return 1 if n == 0 else \
         7*(n-1)+F(n-1)

def isPrime( n ):
  return all(
         n % d != 0
         for d in range(2,int(n**0.5)+1)
         )

count = 0
for i in range(2,200+1):
  if isPrime(F(i)):
    count += 1

print( count )