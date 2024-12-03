from itertools import permutations

pool = [ [ '1', '00100', '00101', '0011' ],
         [ '1', '0010', '00110', '00111' ],
         [ '10', '11', '0010', '0011' ],  ]

known = { 'Б': '000', 'С': '01' }
perm = list( permutations([0, 1, 2, 3]) )

def encode( word, dic ):
  return ''.join( [ dic[c] for c in word ] )

minLen = 100
for a, b, c, d in perm:
  for p in pool:
    add = { 'А': p[a], 'К': p[b], 'Р': p[c], 'Т': p[d] }
    full = known | add
    coded = encode( 'БАРАБАС', full )
    if len(coded) <= minLen:
      minLen = len(coded)
      print( coded, f"{int(coded,2):o}", full )