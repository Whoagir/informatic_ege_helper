x = 4*625**1920 + 4*125**1930 - 4*25**1940 - 3*5**1950 - 1960

count = 0
while x > 0:
  if x % 5 == 0:
    count += 1
  x //= 5

print(count)