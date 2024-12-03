data = [int(x) for x in open('17-9.txt')]

def valid( n ):
  b = bin(n)[2:]
  return b.count('1') >= 3 and b.count('0') >= 1

count, ma = 0, 0
for i, n in enumerate(data):
  if i >= 2:
     r = [valid(data[i-2]), valid(data[i-1]), valid(data[i])]
     if r.count(True) >= 2:
        ma = max(ma, data[i-2], data[i-1], data[i] )
        count += 1

print( count, ma )
