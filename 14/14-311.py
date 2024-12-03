x = 81**18 - (81**8 - 1)*((8 + 1)**8 + 1) // 8 - 8
count1 = 0
while x:
  if x % 3 == 1:
    count1 += 1
  x //= 3

print(count1)