sums = set()
X = 0
while True:
  N = 3*16**2018 - 2*8**1028 - 3*4**1100 - 4**X - 2022
  if N <= 0: break
  s = 0
  while N:
    s += N % 4
    N //= 4
  sums.add( s )
  X += 1

print( len(sums) )

# Автор: Е. Джобс

sums = set()
for d in range(2018*2 + 1):
    x = 3*16**2018 - 2*8**1028 - 3*4**1100 - 4**d - 2022
    s = 0
    while x > 0:
        s += x % 4
        x //= 4
    sums.add(s)
print(len(sums))
