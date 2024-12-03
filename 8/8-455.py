from itertools import product

count = 0
for w in product('012345678',repeat=5):
  if w[0] != '0' and w.count('0') == 1:
    pos = w.index('0')
    if w[pos-1] in '2468' and (pos == 4 or w[pos+1] in '2468'):
       count += 1

print ( count )

#-----------------------------------------------
count = 0
for w in product('012345678',repeat=5):
  s = ''.join(w) + '2'
  if s[0] != '0' and s.count('0') == 1:
    pos = s.find('0')
    if s[pos-1] in '2468' and s[pos+1] in '2468':
       count += 1

print ( count )


