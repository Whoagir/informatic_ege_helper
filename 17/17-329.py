data = [int(x) for x in open("17-328.txt")]
N = len(data)

spec = [ x for x in data if x % 50 != 0 ]
M = max(spec)

def isPalindrome( n ):
  s = str(n)
  return s == s[::-1]

def valid( a, b, c ):
  a, b, c = sorted( [a, b, c] )
  return isPalindrome(a+b) and isPalindrome(a+c) and isPalindrome(b+c) and \
         b + c < M

count, ma = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if ma == None or s > ma:
       ma = s

print( count, ma )

