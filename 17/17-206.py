count = 0
ma = -10**10
with open("17-205.txt") as F:
  prev = int(F.readline())
  while True:
    s = F.readline()
    if not s: break
    x = int(s)
    if (x % 7 == 0 or prev % 7 == 0) and \
       ((x + prev) % 5 == 0):
      ma = max(ma, x + prev)
      count += 1
    prev = x

print( count, ma )
