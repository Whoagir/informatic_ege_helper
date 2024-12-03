N = 1000
for n in range(201,N):
  s = '8'*n
  while '555' in s or '888' in s:
    s = s.replace('555', '8', 1)
    s = s.replace('888', '55', 1)
  if s.count('8') > s.count('5'):
    break

print( n )
