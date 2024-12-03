x = 7*729**543 - 6*81**765 - 5*9**987 - 20

count = 0
while x > 0:
  if x % 9 == 8:
    count += 1
  x //= 9

print( count )