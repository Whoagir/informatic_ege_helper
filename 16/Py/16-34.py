def F(n):
  #print(n)
  out.append( n )
  if n>0:
    d=n%10+F(n//10)
    #print(d)
    out.append( d )
    return d
  else: return 0

n = 1
while True:
  out = []
  res = F(n)
  if out[1] > 51:
    print( n, res )
    break
  n += 1



