digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def toBase( n, b ):
  return digits[n] if n < b else \
         toBase(n//b, b) + digits[n%b]

def alg( n ):
  s = s0 = toBase( n, 20 )
  for _ in range(2):
    for c in 'AEI':
      s = s.replace(c,'1')
    s += digits[n%20]
    s = s[1:] + s[0]
  return int(s, 20), s0

results = []
for N in range(10_000, 100_000):
  R, s = alg(N)
  if R % 2030 == 0:
    results.append( (R, s) )

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
w=[]
for n in range(10000,100000):
    s=ff(n,20)
    s=s.replace('A','1').replace('I','1').replace('E','1')
    s+=f[n%20]
    s=s[1:]+s[0]
    s=s.replace('A','1').replace('I','1').replace('E','1')
    s+=f[n%20]
    s=s[1:]+s[0]
    r=int(s,20)
    if r% 2030==0: w.append(r)
print(max(w))

