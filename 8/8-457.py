from itertools import product

count = 0
for w in product('012345678',repeat=6):
  if w[0] not in '01357' and w[-1] not in '23' and \
     w.count('1') >= 2:
    count += 1

print ( count )

#---------------------------
digits = "012345678"
count = 0
for a in "2468":
 for b in digits:
  for c in digits:
   for d in digits:
    for e in digits:
     for f in "0145678":
      s = a + b + c + d + e + f
      if s.count("1") >= 2:
        count += 1

print(count)
