nn = 652

sumOsn = 0
for base in range(2,11):
    nBase = ""
    n = nn
    OK = True
    while n:
      nBase = str(n % base) + nBase
      if (n % base) == 2:
        OK = False
      n //= base
    if OK:
        sumOsn += base
        print( base, nBase ) # отладочная

print( sumOsn )  # Ответ: 31

