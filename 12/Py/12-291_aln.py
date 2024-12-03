# Автор: А.Л. Наймушин

min5=10
endi = 0
ends = ''
for i in range(401,450):
  s = i*'5'
  while '5555' in s:
    s = s.replace( "5555", "8", 1 )
    s = s.replace( "88", "5", 1 )
  if s.count('5') < min5:
      min5 = s.count('5')
      endi = i
      ends = s
for i in range(401,450):
   if i == endi:
       print('Конечная строка = ',ends)
       print('Наименьшая длина исходной строки = ',endi)
       print('Наименьшее число цифр 5 = ',min5)
       break
'''
Ответ:
Конечная строка =  8
Наименьшая длина исходной строки =  403
Наименьшее число цифр 5 =  0
'''
