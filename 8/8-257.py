from itertools import product

words = [ ''.join(x) for x in product('СТЕПУХА', repeat=4) ]
words = words[1000:]

count = 0
for w in words:
  if all( a != b for a, b in zip(w, w[1:]) ):
    count += 1

print( count )

