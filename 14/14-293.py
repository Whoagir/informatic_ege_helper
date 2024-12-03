x = 0
s = 0
while s != 71:
   x += 1
   a = 64**11 - 4**10 + 96 - x
   s = 0
   while a > 0:
       s += a % 4
       a = a // 4
print(x)
