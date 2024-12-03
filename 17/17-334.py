data = [int(x) for x in open("17-1.txt")]
N = len(data)
dataSet = set( data )

M = min( x for x in data if x > 0 and x % 15 == 0 )

def valid( a, b ):
  return a % 2 == 1 and b % 2 == 1 and (a+b)//2 >= M

count, mi = 0, 100001
for i in range(N-1):
   if valid( data[i], data[i+1] ):
     mi1 = (data[i] + data[i+1]) // 2
     count += 1
     if mi1 < mi: mi = mi1

print( count, mi )

