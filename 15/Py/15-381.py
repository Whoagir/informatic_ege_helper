def Del(x, d):
  return x % d == 0

def f(x, A):
  return ((not Del(x, A)) or Del(x, 36) and Del(x, 126)) and (A > 1000)

start = 1
MAX = 20000

for A in range(start, 2000):
  OK = 1
  for x in range(1, MAX):
    if not f(x,A):
      OK = 0
      break
  if OK:
    print(A)
    break



