data = [ int(x) for x in open("17-360.txt") ]

def prodDigits( n ):
  p = 1
  for c in str(abs(n)):
    p *= int(c)
  return p

max42 = max( x for x in data if prodDigits(x) % 100 == 42 )

from itertools import product

count = 0
minProd = 10**10
for triple in zip(data, data[1:], data[2:]):
   if any( triple[i]+triple[j] == 0
           for i, j in product([0, 1, 2], repeat = 2) ) and \
      all( x < max42 for x in triple ):
      count += 1
      for i, j in product([0, 1, 2], repeat = 2):
        if triple[i]+triple[j] == 0:
          minProd = min( minProd, abs(triple[i])**2 )
          break

print( count, minProd )



