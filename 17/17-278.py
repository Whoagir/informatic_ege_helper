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
  if x % 32 == 0:
    s += 3*toBase(x, 5).count('3')

count, ma = 0, 0
for i in range(len(data)-2):
  if data[i] > s or data[i+1] > s or data[i+2] > s:
    count += 1
    ma = max( ma, data[i]+data[i+1]+data[i+2] )

print( count, ma )    
  