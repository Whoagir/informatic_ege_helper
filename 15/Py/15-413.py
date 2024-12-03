def Del(x, d):  return x % d == 0
def nDel(x, d): return x % d != 0

dd = [12, 530, 170]
def f(x, A):
  return Del(A,dd[0]) and \
         ( Del(dd[1], x) <= (nDel(A, x) <= nDel(dd[2],x)) )

start = 1
MAX = 20000

count = 0
for A in range(start, 1000+1):
  OK = 1
  for x in range(1, MAX):
    if not f(x,A):
      OK = 0
      break
  if OK:
    print(A)
    count += 1

print("Всего: ", count )

