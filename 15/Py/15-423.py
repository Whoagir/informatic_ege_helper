def nD( n, m ):
  return not D(n, m)
def D( n, m ):
  return (n % m) == 0

def f(x, A):
  return D(A, 5) and (nD(2020,A) <= (D(x,1718) <= D(2023,A)) )

Q = list(range(27, 49+1))

start = 1
MAX = 60000
count = 0
for A in range(start, 50000+1):
  OK = 1
  for x in range(1, MAX):
    if not f(x,A):
      OK = 0
      break
  if OK:
    print(A)
    count += 1

print(count)