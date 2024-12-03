def alg( s ):
  while '111' in s or '222' in s:
    if '111' in s:
      s = s.replace('111', '22', 1)
    else:
      s = s.replace('222', '11', 1)
  return s

sMax = ''
for i in range(0,204):
  s = ['1']*204
  s[i] = '2'
  sResult = alg( "".join(s) )
  if len(sResult) > len(sMax):
    print( i, sResult )
    sMax = sResult

print( sMax )