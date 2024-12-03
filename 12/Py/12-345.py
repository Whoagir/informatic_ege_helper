
for n in range(3,10000+1):
  s = '5' + '2'*n
  while '72' in s or '522' in s or '2222' in s:
    s = s.replace('72', '2', 1)
    s = s.replace('522', '27', 1)
    s = s.replace('2222', '5', 1)
  sumDig = sum(map(int, s))
  if sumDig == 63:
    print( n )
    break
