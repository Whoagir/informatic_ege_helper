nn = 804

sumOsn = 0
for base in range(2,11):
    OK = False
    nBase = ""
    n = nn
    while n:
      nBase = str(n % base) + nBase
      if (n % base) == 1:
        OK = True
      n //= base
    if OK:
        sumOsn += base
        print( base, nBase ) # отладочная

print( sumOsn )  # Ответ: 31

