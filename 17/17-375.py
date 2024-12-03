data = [int(x) for x in open('17-375.txt')]

min3 = min( x for x in data if 100 <= x < 1000 and
              len(str(x)) == len(set(str(x))) )
N = len(data)
res = []
i, j = 0, N-1
while i < j:
  if data[i]*data[j] % min3 == 0:
    res.append( data[i] + data[j] )
  i += 1
  j -= 1

print( len(res), min(res) )

