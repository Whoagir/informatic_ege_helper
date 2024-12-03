data = [ int(x) for x in open("17-301.txt") ]
N = len(data)

def sumDigits( n ):
  return sum( map(int, str(n)) )

sum12 = sum( sumDigits(x) for x in data if x % 12 == 0 )

def valid( a, b, c ):
  return ((a % (sumDigits(b) + sumDigits(c)) == 0) +
          (b % (sumDigits(a) + sumDigits(c)) == 0) +
          (c % (sumDigits(a) + sumDigits(b)) == 0)) == 1

count, ma = 0, None
for i in range(N-2):
   s = sum(data[i:i+3])
   if valid(data[i], data[i+1], data[i+2]) and s < sum12:
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

