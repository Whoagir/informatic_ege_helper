# Автор: PRO100-ЕГЭ

from itertools import permutations

table = "14 17 24 26 36 41 42 45 46 47 54 56 57 62 63 64 65 71 74 75"
graph = "аб ба бв вб бж жб бе еб вж жв еж же ед де жг гж жд дж гд дг"

for per in permutations("абвгдеж"):
  new_graph = table
  for i in range(1,8):
    new_graph = new_graph.replace( str(i), per[i-1] )
  if set(graph.split()) == set(new_graph.split()):
    print( *enumerate(per, start=1) )