def Del(x, d):
  return x % d == 0
def nDel(x, d):
  return x % d != 0

dd = [144, 18, 24]
def f(x, A):
  return Del( dd[0], A) and \
         ( nDel(x, A) <= (Del(x, dd[1]) <= nDel(x, dd[2])) )

start = 1
MAX = 20000

for A in range(start, 1000):
  OK = 1
  for x in range(1, MAX):
    if not f(x,A):
      OK = 0
      break
  if OK:
    print(A)

#------------------------------
def D(x, d): return x % d == 0
def nD(x, d): return x % d != 0
def f(x, A):
  return D(144, A) and (nD(x, A) <= (D(x, 18) <= nD(x, 24)))

print( max(
A for A in range(1,1000)
    if all( f(x,A) for x in range(1,1000) )
)
)

