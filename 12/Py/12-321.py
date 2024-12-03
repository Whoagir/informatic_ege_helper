
for n in range(1,1000):
  s = '>2' + '12'*n + '<'
  while '>2<' not in s:
    s0 = s
    s = s.replace('>1', '>2', 1)
    s = s.replace('12<', '1<2', 1 )
    s = s.replace('>21', '1>', 1)
    s = s.replace('1<', '<2', 1)
    if s0 == s: break
  if '>2<' in s:
    sumDigits = sum( map(int, (c for c in s if c in '12') ) )
    if sumDigits > 103:
      print( n, s )
      break


