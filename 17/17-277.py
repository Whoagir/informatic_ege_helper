data = [ int(x) for x in open('17-277.txt') ]

def toBase( n, base ):
  s = ''
  n = abs(n)
  while n:
    s = str(n%base) + s
    n //= base 
  return s

s = 0
for x in data:
  if x % 60 == 0:
    s += 2*toBase(x, 3).count('2')

count, ma = 0, -20001
for i in range(len(data)-1):
  if data[i] > s or data[i+1] > s:
    count += 1
    ma = max( ma, data[i]+data[i+1] )

print( count, ma )    
  