data = [int(x) for x in open("17-333.txt")]
N = len(data)
dataSet = set( data )

spec = [ x for x in data if 1000 <= x <= 9999 ]
M = sum(spec) / len(spec)

def valid( s ):
  return s not in dataSet and s < M

def sumDigits( n ):
  return sum( map(int, str(n)) )

count, ma = 0, 0
for i in range(N-1):
   s = data[i] + data[i+1]
   if valid( s ):
     s = sumDigits(data[i]) + sumDigits(data[i+1])
     count += 1
     if s > ma: ma = s

print( count, ma )

