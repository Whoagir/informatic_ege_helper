def Del(x, d):
  return x % d == 0

def f(x, A):
  return ((Del(x, A) and Del(x, 45)) <= Del(x, 162)) and (A > 200)

start = 200
MAX = 20000

for A in range(start, 1000):
  OK = 1
  for x in range(1, MAX):
    if not f(x,A):
      OK = 0
      break
  if OK:
    print(A)
    break



