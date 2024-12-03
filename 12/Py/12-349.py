
for n in range(1, 1000):
  s = '7' + '1'*(n+1) + '2'*(n+2) + '3'*(n+3)
  while '71' in s or '72' in s or '73' in s:
    s = s.replace( '71', '227', 1)
    s = s.replace( '72', '37', 1)
    s = s.replace( '73', '17', 1)
  sumDig = sum( map(int, s) )
  if sumDig == 9*n:
    print(n)
    break
