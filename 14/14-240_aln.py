# Автор: А. Наймушин
# задача 14.240

x = (729**41-81**16)*(729**15+9**5)
#print (x)
count0 = 0
s = ''
while x:
    s += str(x % 9)
    #print (s)
    if x % 9 == 0:
      count0 += 1
      #print (x)
    x //= 9
print( 'Ответ:', count0 )

# Ответ: 77

