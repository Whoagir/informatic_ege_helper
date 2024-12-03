data = [int(x) for x in open("17-332.txt")]
N = len(data)

spec = [ x for x in data if x % 17 != 0 ]
M = sum(spec) / len(spec)

def sumDigits( n ):
  return sum( map(int, str(n)) )

def valid( a, b, c ):
  return sumDigits(a) == sumDigits(c) and b < M

count = 0
sumCount = [0]*(4*9+1)
for i in range(N-2):
   s = sumDigits( data[i+1] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     sumCount[s] += 1

print( count, sumCount.index(max(sumCount)) )

