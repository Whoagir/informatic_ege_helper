
def alg( s ):
  while '15' in s or '16' in s or '17' in s:
    if '15' in s:
      s = s.replace('15', '7616', 1)  # +1
    if '16' in s:
      s = s.replace('16', '51', 1)  # +1
    if '17' in s:
      s = s.replace('17', '615', 1)  # +1
  return s

s = '1' + 65*'5' + 17*'6' + 44*'7'
r = alg(s)

print( r.count('1'),  r.count('5'), r.count('6'), r.count('7')  )

print( s.count('6') )



