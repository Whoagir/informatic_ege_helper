from itertools import product

def valid(s):
  s = [' '] + list(s) + [' ']
  for i in range(1,len(s)-1):
     if s[i] == 'A' and s[i-1] != 'D' and s[i+1] != 'D':
        return False
     if s[i] == 'C' and ((s[i-1] == 'B') or (s[i+1] == 'B')):
        return False
  return True

candidates = product('ABCD', repeat=3)

v = [s for s in candidates if valid(s)]

print( len(v) )

