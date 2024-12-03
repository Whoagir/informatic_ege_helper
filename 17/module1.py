from random import randint

N = 70000
with open("17-403.txt", "w") as F:
  for i in range(N):
    k = randint(2,5)
    if k == 2: x = randint(32,100)
    if k == 3: x = randint(100,999)
    if k == 4: x = randint(1000,9999)
    if k == 5: x = randint(10000,99999)
    print( x, file=F )

