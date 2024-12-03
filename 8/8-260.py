from itertools import permutations

Alpha = 'ТИХОРЕЦК'
Glas = 'ИОЕ'

def valid( s ):
  nGlas = sum( s.count(c) for c in Glas )
  if nGlas != 2: return False
  return sum( c == c1 for c, c1 in zip(s,'ТИХО')) == 2

count = 0
for w in permutations( Alpha, 4 ):
   if valid( "".join(w) ):
      count += 1

print( count )