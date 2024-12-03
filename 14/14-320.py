x = 1*3**37 + 2*3**23 + 3*3**20 + 4*3**4 + 5*3**3 + 4 + 5
count0 = 0
while x:
  if x % 9 == 0:
    count0 += 1
  x //= 9

print( count0 )

# задача 14.320
x = 1*3**37 + 2*3**23 + 3*3**20 + 4*3**4 + 5*3**3 + 4 + 5

count0 = 0
s = ''
while x != 0:
    s = str(x % 9) + s
    #print (s)
    if x % 9 == 0:
      count0 += 1
      #print (x)
    x //= 9
print('s = ',s, '  Ответ:', count0 )

# Ответ: 14
