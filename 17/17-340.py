data = [int(x) for x in open( '17-340.txt' )]
N = len(data)
all22 = [ x for x in data if x % 22 == 0 ]
M = sum(all22) / len(all22)

def valid( a, b ):
  sa = f'{a:o}'
  sb = f'{b:o}'
  return sa.index(max(sa)) < sa.index(min(sa)) and \
         sb.index(max(sb)) < sb.index(min(sb)) and \
         a + b < M

count, ma = 0, 0
for i in range(N-1):
  if valid( data[i], data[i+1]):
    count += 1
    ma = max( ma, data[i]+data[i+1] )

print( count, ma )