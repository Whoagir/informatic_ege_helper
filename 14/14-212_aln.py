# Автор: А. Наймушин
# задача 14.212

x = 36**17+6**48-17
print (x)
count0 = 0
s = ''
while x:
    s += str(x % 6)
    #print (s)
    if x % 6 == 0:
      count0 += 1
      #print (x)
    x //= 6
print('s = ',s, '  Ответ:', count0 )

# Ответ: 14
