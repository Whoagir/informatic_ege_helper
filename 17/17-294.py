data = [ int(x) for x in open("17-294.txt") ]

def isSquare( n ) :
  q = round(n**0.5)
  return q*q == n

def sumDigits( n ):
  return sum( map(int, str(n)) )

N = len(data)
av = sum(data) / N

count, ma = 0, None
for i in range(N-1):
   pair = data[i:i+2]
   sDigits = sumDigits(pair[0]) + sumDigits(pair[1])
   if isSquare(sDigits) and sum(pair) > av:
     count += 1
     if ma == None or sDigits > ma:
       ma = sDigits

print( count, ma )
