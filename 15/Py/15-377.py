def Del(x, d):
  return x % d == 0

def f(x, A):
  return ( ((Del(x, 12) or Del(x, 36)) <= Del(x, A)) and
           (A*A - A - 90 < 0) )

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



