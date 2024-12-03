from itertools import product

digits8 = '01234567'
digits8x = '1234567'
even = ' 0246'

count = 0
for d5 in digits8x:
  for d4, d3, d2, d1, d0 in product(digits8, repeat=5):
    s = f' {d5}{d4}{d3}{d2}{d1}{d0} '
    if s.count('6') == 2:
      pos61 = s.find('6')
      pos62 = s.rfind('6')
      if s[pos61-1] in even and s[pos61+1] in even and \
         s[pos62-1] in even and s[pos62+1] in even:
        count += 1

print( count )

