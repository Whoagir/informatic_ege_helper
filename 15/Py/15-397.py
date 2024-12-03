def Del(x, d):
  return x % d == 0

dd = [108, 42, 68]
def f(x, A):
  return ( Del( dd[0], A) and
           ( (not Del(x, A)) <= (Del(x, dd[1]) <= (not Del(x, dd[2])) )) )

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



