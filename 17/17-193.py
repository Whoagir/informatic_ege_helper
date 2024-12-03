data = [int(x) for x in open('17-8.txt')]

def valid( n ):
  s = sum(map( int, bin(n)[2:] ))
  return s > 5 and s % 2 == 1

count, ma = 0, 0
for i, n in enumerate(data):
  if i > 0:
    if valid(data[i-1]) or valid(data[i]):
      count += 1
      ma = max(ma, data[i-1] + data[i] )

print( count, ma )
