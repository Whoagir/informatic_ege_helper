nn = 432

sumOsn = 0
for base in range(2,11):
    OK = True
    prev = -1
    nBase = ""
    n = nn
    while n:
      nBase = str(n % base) + nBase
      if (n % base) < prev:
        OK = False
        break
      prev = n % base
      n //= base
    if OK:
        sumOsn += base
        print( base, nBase ) # отладочная

if sumOsn > 0:
  print( sumOsn )  # Ответ: 33
