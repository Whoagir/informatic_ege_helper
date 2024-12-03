def z( n, m ):
  return (n & m ) == 0

def f(x, A):
  return z(x, 13) <= ( (not z(x,40)) <= (not z(x,A)) )

start = 1
MAX = 20000

for A in range(start, 1000+1):
  OK = 1
  for x in range(1, MAX):
    if not f(x,A):
      OK = 0
      break
  if OK:
    print(A)
    break
