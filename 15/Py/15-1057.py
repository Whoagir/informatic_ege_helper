def f(x, y, A):
  return (x*y < A) or (x >= 16) or (x < 5*y)

start = 1
MAX = 200

for A in range(start, 100):
  OK = 1
  for x in range(1, MAX):
    for y in range(1, MAX):
      if not f(x, y, A):
        OK = 0
        break
    if not OK:
      break
  if OK:
    print(A)
    break



