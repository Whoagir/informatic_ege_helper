# Автор: А.Л. Наймушин

min5 = 10
endi = 0
ends = ''
for i in range(251,400):
  s = i*'5'
  while '55555' in s:
    s = s.replace( "55555", "88", 1 )
    s = s.replace( "888", "555", 1 )
  if s.count('5') < min5:
      min5 = s.count('5')
      endi = i
      ends = s
for i in range(251,400):
   if i == endi:
       print('Конечная строка = ',ends)
       print('Наименьшая длина исходной строки = ',endi)
       print('Наименьшее число цифр 5 = ',min5)
       break
'''
Ответ:
Конечная строка =  885
Наименьшая длина исходной строки =  258
Наименьшее число цифр 5 =  1
'''