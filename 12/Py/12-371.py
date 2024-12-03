def alg( s ):
  while '00' not in s:
    s = s.replace('01', '320', 1)
    s = s.replace('02', '2013', 1)
    s = s.replace('03', '1210', 1)
  return s

# 1 -> 32
# 2 -> 2013 -> 23203 -> 232121
# 3 -> 121

maxLen = 0
for k1 in range(50):
  for k2 in range(50):
    for k3 in range(50):
      s = '0' + '1'*k1 + '2'*k2 + '3'*k3 + '0'
      r = alg( s )
      m1 = r.count('1')
      m2 = r.count('2')
      if [m1, m2] == [36, 30]:
        curLen = k1 + k2 + k3
        maxLen = max( curLen, maxLen )

print( maxLen + 2 )
