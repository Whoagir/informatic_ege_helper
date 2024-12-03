
def f( n ):
  return n if n < 10 else \
         f(n//10) + f(n%10) if n < 1000 else \
         f(n//1000) - f(n%1000)

print( sum(1 for n in range(10**6) if f(n) == 0) )


from itertools import product
count = 0
for a, b, c, a1, b1, c1 in product(range(10), repeat=6):
  if a+b+c == a1+b1+c1:
    count += 1
print(count)