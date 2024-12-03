def f(n):
  return n*n + 5*n + 4 if n > 30 else \
         f(n+1) + 3*f(n+4) if n % 2 == 0 else \
         2*f(n+2) + f(n+5)

count = 0
for n in range(1,1001):
  fn = str(f(n))
  if sum(map(int, fn)) == 27:
    count += 1

print(count)
