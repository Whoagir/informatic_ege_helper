# Автор: А. Наймушин
# задача 14.238

x = (512**78 - 512**60)*(512**5+64**5)
#print (x)
count7 = 0

while x:

    #print (s)
    if x % 8 == 7:
      count7 += 1
      #print (x)
    x //= 8
print( 'Ответ:', count7 )

# Ответ: 53


