digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def toBase( n, b ):
  return digits[n] if n < b else \
         toBase(n//b, b) + digits[n%b]

def alg( n ):
  s = s0 = toBase( n, 19 )
  for _ in range(2):
    for c in 'BCDFGH':
      s = s.replace(c,'5')
    s = digits[n%19] + s
    s = s[-2:] + s[:-2]
  return int(s, 19), s0

results = []
for N in range(100_000, 1_000_000):
  R, s0 = alg(N)
  sumDigits = sum( map(int, str(R)) )
  if sumDigits % 7 == 0:
    results.append( (R, s0) )

print( max(results) )

#----------------------------------------
# Автор: П. Финкель

f='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def ff(a,b):
    x=''
    while a>0:
        x=f[a%b]+x
        a=a//b
    return x


w = []
for n in range(100000,1000000):
    s=ff(n,19)
    s=s.replace('B','5').replace('C','5').replace('D','5').replace('F','5').replace('G','5').replace('H','5')
    s=f[n%19]+s
    s=s[-2:]+s[:-2]
    s=s.replace('B','5').replace('C','5').replace('D','5').replace('F','5').replace('G','5').replace('H','5')
    s=f[n%19]+s
    s=s[-2:]+s[:-2]
    r=int(s,19)
    y=sum(map(int,str(r)))
    if y % 7 == 0: w.append(r)

print(max(w))
