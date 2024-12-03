def Z(x, d):
  return x & d == 0

def f(x, A):
  return ((not Z(x,13) or Z(x,A)) <= (not Z(x,13)) ) or (not Z(x, A)) or Z(x, 39)

start = 1
MAX = 1000

for A in range(start, 100):
  OK = 1
  for x in range(1, MAX):
    if not f(x, A):
      OK = 0
      break
  if OK:
    print(A)
    break



