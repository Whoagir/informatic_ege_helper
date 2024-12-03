from itertools import product

count1 = 0
for i in range(10**5, 10**6):
  s = str(i)
  if len(s) == len(set(s)):
    [ s := s.replace(c, '0') for c in  '02468' ]
    [ s := s.replace(c, '1') for c in  '13579' ]
    if '00' not in s and '11' not in s:
      count1 += 1

print( count1 )

count2 = 0
for i in range(10**3, 10**4):
  s = str(i)
  if all( c+c not in s for c in '0123456789' ):
    count2 += 1

print( count2 )

print( count2 - count1)
