def nD( n, m ):
  return (n % m) != 0

def f(x, A):
  return ( nD(x, 3) and x not in [48, 52, 56]) <= \
         (((abs(x - 50) <= 7) <= (x in Q)) or (x & A == 0))

Q = list(range(27, 49+1))

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
