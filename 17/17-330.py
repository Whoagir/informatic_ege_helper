data = [int(x) for x in open("17-328.txt")]
N = len(data)

def sumDigits( a ):
  return sum( sum(map(int, str(x))) for x in a )

spec = [ x for x in data if x % 22 == 0 ]
M = sumDigits( spec )

def isOctEven( n ):
  s = f"{n:o}"
  return all( c in "0246" for c in s )

def valid( a, b, c ):
  return isOctEven(a+b) and isOctEven(a+c) and isOctEven(b+c) and \
         a + b + c < M

count, mi = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

