data = [ int(x) for x in open('17-278.txt') ]

def toBase( n, base ):
  s = ''
  n = abs(n)
  while n:
    s = str(n%base) + s
    n //= base 
  return s

s = 0
for x in data:
  if x % 12 == 0:
    s += 4*toBase(x, 5).count('4')

count, ma = 0, 0
for i in range(len(data)-1):
  if data[i] > s and data[i+1] > s:
    count += 1
    ma = max( ma, data[i]+data[i+1] )

print( count, ma )    
  