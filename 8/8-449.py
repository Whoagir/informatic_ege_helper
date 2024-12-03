from itertools import permutations

A = "ВАРВАРА"

i = 1
for w in sorted(set(permutations(A))):
  s = ''.join(w)
  if i % 2 == 0 and s[0] == 'В' and 'ААА' in s and 'РР' not in s:
    print( i, s )
  i += 1
