from itertools import permutations

pool = [ [ '10', '000', '001', '010'],
         [ '00', '10', '0100', '0101'],
         [ '000', '001', '010', '10'],
           ]

known = { 'К': '011', 'Р': '11' }
perm = list( permutations([0, 1, 2, 3]) )

def encode( word, dic ):
  return ''.join( [ dic[c] for c in word ] )

minLen = 100
for a, b, c, d in perm:
  for p in pool:
    add = { 'П': p[a], 'Л': p[b], 'Е': p[c], 'С': p[d] }
    full = known | add
    coded = encode( 'ПЕРЕПЕЛ', full )
    if len(coded) <= minLen:
      minLen = len(coded)
      print( coded, f"{int(coded,2):o}", full )