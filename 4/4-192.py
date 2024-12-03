from itertools import permutations

pool = [ [ '1', '0100', '0101'],
         [ '010', '10', '11']   ]

known = { 'К': '00', 'Р': '011' }
perm = list( permutations([0, 1, 2]) )

def encode( word, dic ):
  return ''.join( [ dic[c] for c in word ] )

minLen = 100
for a, b, c in perm:
  for p in pool:
    add = { 'О': p[a], 'Г': p[b], 'Н': p[c] }
    full = known | add
    coded = encode( 'КОНОГОН', full )
    if len(coded) <= minLen:
      minLen = len(coded)
      print( coded, f"{int(coded,2):o}", full )