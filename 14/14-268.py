nn = 572

sumOsn = 0
for base in range(2,11):
    nBase = ""
    n = nn
    OK = False
    prev = -1
    while n:
      nBase = str(n % base) + nBase
      if (n % base) == prev:
        OK = True
      prev = n % base
      n //= base
    if OK:
        sumOsn += base
        print( base, nBase ) # отладочная

print( sumOsn )  # Ответ: 16

