x = 0
s = 0
while s != 22:
   x += 1
   a = 27 ** 7 - 3 ** 11 + 36 - x
   s = 0
   while a > 0:
       s += a % 3
       a = a // 3
print(x)
