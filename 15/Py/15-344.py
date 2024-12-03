
def f(x, y, A):
  return (5*x + 3*y != 60) or ((A > x) and (A > y))

start = 1
MAX = 1000

for A in range(start, 1000):
  OK = 1
  for x in range(0, MAX):
    for y in range(0, MAX):
      if not f(x, y, A):
        OK = 0
        break
    if OK == 0: break
  if OK:
    print(A)
    break



