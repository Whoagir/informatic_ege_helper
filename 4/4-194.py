from itertools import permutations

pool = [ [ '00', '01', '1100', '1101' ],
         [ '000', '001', '01', '110' ],
         [ '00', '010', '011', '110' ],  ]

known = { 'А': '10', 'К': '111' }
perm = list( permutations([0, 1, 2, 3]) )

def encode( word, dic ):
  return ''.join( [ dic[c] for c in word ] )

minLen = 100
for a, b, c, d in perm:
  for p in pool:
    add = { 'Л': p[a], 'О': p[b], 'С': p[c], 'Т': p[d] }
    full = known | add
    coded = encode( 'КОЛОКОЛ', full )
    if len(coded) <= minLen:
      minLen = len(coded)
      print( coded, f"{int(coded,2):o}", full )