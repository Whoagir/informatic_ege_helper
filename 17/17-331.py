data = [int(x) for x in open("17-328.txt")]
N = len(data)

spec = [ x for x in data if x % 2 != 0 ]
M = sum(spec) / len(spec)

def isOk( a ):
  return '7' not in f"{a:o}"

def valid( a, b, c ):
  return isOk(a+b) and isOk(a+c) and isOk(b+c) and \
         a + b + c < M

count, ma = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

