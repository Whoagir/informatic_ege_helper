def alg( n ):
  s = f"{n:b}"
  s = f"{int(n)-s.count('0'):b}"
  return int( s[-3:] + s, 2 )

rr = []
for n in range(13, 100):
  if alg(n) > 224:
    rr.append( alg(n) )

print( min(rr) )


# Автор: Е. Джобс

s = set()
for i in range(1, 225):
    n = i - bin(i)[2:].count('0')
    b_n = bin(n)[2:]
    if len(b_n) >= 3:
        b_n = b_n[-3:] + b_n
        b = int(b_n, 2)
        if b > 224:
            s.add(b)
print(min(s))


