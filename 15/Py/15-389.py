def Del(x, d):
  return x % d == 0

def f(x, A):
  return ( Del(21, A) and ( (Del(x, 40) and Del(x, 30)) <= Del(x, A)))

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



