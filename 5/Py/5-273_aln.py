
#5.273_Aвтор А.Л.Наймушин

def alg( x ):
  s = bin(x)[2:]
  if x%2 == 1:
    s = '1' + s + '0'
  else:
    s = '11' + s + '11'
    
  return int(s, 2)


for i in range(1000,1,-1):
  if i%2==0 and alg(i)<126:
    print( i,alg(i))
    break

'''
6 123
'''
