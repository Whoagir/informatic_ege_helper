# Автор: А.Л. Наймушин

max5 = 0
endi = 0
ends = ''
for i in range(201,250):
  s = i*'5'
  while '55555' in s:
    s = s.replace( "55555", "88", 1 )
    s = s.replace( "888", "55", 1 )
  if s.count('5') > max5:
      max5 = s.count('5')
      endi = i
      ends = s
for i in range(201,250):
   if i == endi:
       print('Конечная строка = ',ends)
       print('Наименьшая длина исходной строки = ',endi)
       print('Наибольшее число цифр 5 = ',max5)
       break
'''
Ответ:
Конечная строка =  5585555
Наименьшая длина исходной строки =  201
Наибольшее число цифр 5 =  6
'''
