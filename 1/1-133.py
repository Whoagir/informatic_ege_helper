# Автор: Джабраил Айдиев

from itertools import permutations

mat = [{3, 7}, {3, 6, 7}, {1, 2, 5}, {5, 6}, {3, 4}, {2, 4, 7}, {1, 2, 6}]

for a, b, c, d, e, f, g in permutations(range(1,8)):
  cnt =	[0]*7
  cnt[a-1] = {d, b, f}
  cnt[b-1] = {a, f,	e}
  cnt[c-1] = {f, g}
  cnt[d-1] = {a, e}
  cnt[e-1] = {d, b, g}
  cnt[f-1] = {a, b, c}
  cnt[g-1] = {e, c}
  if cnt == mat:
    print( a, b, c,	d, e, f, g )
