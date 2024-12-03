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
  s += 7*toBase(x, 8).count('7')

count, mi = 0, 20000
for i in range(len(data)-1):
  if data[i] > s and data[i+1] > s:
    count += 1
    mi = min( mi, data[i]+data[i+1] )

print( count, mi )    
  