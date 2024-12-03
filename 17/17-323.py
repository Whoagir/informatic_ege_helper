data = [int(x) for x in open("17-316.txt")]
N = len(data)

def sumDigits( n ):
  return sum( int(x) for x in str(n) )

sumAllDigits = sum( sumDigits(x) for x in data )

def valid( a, b, c ):
  digits = [ int(d) for d in str(a*b*c) ]
  return all( d in digits for d in range(10) ) and \
         (a + b + c) < sumAllDigits

count, mi = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

