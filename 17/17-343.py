data = [ int(x) for x in open('17-343.txt') ]
N = len(data)

def valid( n ):
  s = [ 0, 0 ]
  i = 0
  while n:
    s[i] += n % 10
    i = 1 - i
    n //= 10
  return s[0] and (s[1] % s[0] == 0)

def validTrio( a, b, c ):
  return valid(a) and valid(b) and valid(c)

count, mi = 0, None
for i in range(N-2):
  if validTrio( data[i], data[i+1], data[i+2] ):
    count += 1
    s = sum(data[i:i+3])
    if mi == None or s < mi:
      mi = s

print( count, mi )

