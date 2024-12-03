nn = 364

sumOsn = 0
for base in range(2,11):
    OK = True
    prev = -1
    nBase = ""
    n = nn
    while n:
      nBase = str(n % base) + nBase
      if not(prev < 0 or (n % base) == prev):
        OK = False
        break
      prev = n % base
      n //= base
    if OK:
        sumOsn += base
        print( base, nBase ) # отладочная

print( sumOsn )  # Ответ: 12

