nn = 1755

sumOsn = 0
for base in range(2,11):
    OK = True
    prev = []
    nBase = ""
    n = nn
    while n:
      nBase = str(n % base) + nBase
      if (n % base) in prev:
        OK = False
        break
      prev.append( n % base )
      n //= base
    if OK:
        sumOsn += base
        print( base, nBase ) # отладочная

print( sumOsn )  # Ответ: 15

