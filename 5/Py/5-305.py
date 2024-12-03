def sumHexDigits( s ):
  res = sum( int(x,16) for x in s )
  return res

n = 1
while True:
  s = f"{n:X}" + ('F' if n % 2 == 0 else '0')
  for _ in range(2):
    s += f"{sumHexDigits(s) % 16:X}"
  if s.count(max(s)) == 5*s.count(min(s)):
    print( n, s )
    break
  n += 1
