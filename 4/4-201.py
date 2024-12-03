from itertools import permutations

pool = [ [ '00', '01', '1110', '1111' ],
         [ '0', '1110', '11110', '11111' ], ]

known = { 'П': '1101', 'А': '10', 'Р': '1100' }
perm = list( permutations([0, 1, 2, 3]) )

def encode( word, dic ):
  return ''.join( [ dic[c] for c in word ] )

minLen = 100
for a, b, c, d in perm:
  for p in pool:
    add = { 'В': p[a], 'И': p[b], 'Л': p[c], 'О': p[d] }
    full = known | add
    coded = encode( 'ПОВРАЛИПОПРАВО', full )
    if len(coded) <= minLen:
      minLen = len(coded)
      print( coded[::-1], len(coded), { let: code[::-1] for let, code in full.items() } )