# Автор: А.Л. Наймушин

max5=0
endi = 0
for i in range(501,510):
  s = i*'5'
  while '5555' in s:
    s = s.replace( "5555", "8", 1 )
    s = s.replace( "88", "5", 1 )
  if s.count('5') > max5:
      max5 = s.count('5')
      endi = i
for i in range(501,510):
   if i == endi:
       print(endi,max5)
       break
#Rez = 504 3
