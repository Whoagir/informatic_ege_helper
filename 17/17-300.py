data = [ int(x) for x in open("17-300.txt") ]
N = len(data)

def sumDigits( n ):
  return sum( map(int, str(n)) )

max401 = max( x for x in data if x % 401 == 0 )

def valid( a, b, c ):
  return a % (sumDigits(b) + sumDigits(c)) == 0 or \
         b % (sumDigits(a) + sumDigits(c)) == 0 or \
         c % (sumDigits(a) + sumDigits(b)) == 0

count, mi = 0, None
for i in range(N-2):
   s = sum(data[i:i+3])
   if valid(data[i], data[i+1], data[i+2]) and s > max401:
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

