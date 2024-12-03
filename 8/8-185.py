A = "0123456789"

A = list( reversed(A) )
AA = [ [], [] ]
AA[0] = [int(x) for x in A if ord(x) % 2 == 0]
AA[1] = [int(x) for x in A if ord(x) % 2 != 0]

def valid( n ):
  dPrev = n // 100000
  k = dPrev % 2
  s = str(n)
  for i in range(1,len(s)):
    d = int(s[i])
    if d >= dPrev: return False
    k = 1 - k
    if not (d in AA[k]): return False
    dPrev = d
  return True

valid( 876543 )

count = 0
for n in range(100000, 1000000):
  if valid(n):
    count += 1
    print(n)

print(count)
