# Автор В. Ганиев

data = [ int(x) for x in open('17-276.txt') ]

from itertools import permutations
ans = []
for i in range(len(data)-2):
  for a, b, c in permutations(data[i:i+3]):
    d = b // a
    if d > 1 and b**2 == a*c:
      ans.append( d**2 )
      break

print( len(ans), max(ans) )