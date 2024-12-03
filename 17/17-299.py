data = [ int(x) for x in open("17-299.txt") ]
N = len(data)

def sumDigits( n ):
  return sum( map(int, str(n)) )

sum50 = sum( sumDigits(x) for x in data if x % 50 == 0 )

def valid( a, b, c ):
  return a in [sumDigits(b), sumDigits(c)] or \
         b in [sumDigits(a), sumDigits(c)] or \
         c in [sumDigits(a), sumDigits(b)]

count, ma = 0, None
for i in range(N-2):
   s = sum(data[i:i+3])
   if valid(data[i], data[i+1], data[i+2]) and s < sum50:
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

