# Автор: А.Л. Наймушин

max5=0
endi = 0
for i in range(301,350):
  s = i*'5'
  while '55555' in s:
    s = s.replace( "55555", "88", 1 )
    s = s.replace( "888", "55", 1 )
  if s.count('5') > max5:
      max5 = s.count('5')
      endi = i
for i in range(301,350):
   if i == endi:
       print(endi,max5)
       break
'''
Ответ: 311 6
'''
