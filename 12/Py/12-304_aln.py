#12.304_Aвтор_А.Л.Наймушин

for x in range(0,50):
 for y in range(0,50):
  for z in range(0,50):
    s = "0" + '1'*x + '2'*y + '3'*z + '0'
    while '00' not in s:
      s = s.replace( '01', '21022', 1 )
      s = s.replace( '02', '310', 1 )
      s = s.replace( '03', '230112', 1 )
    if s.count('1') == 104 and s.count('2') == 39 and s.count('3') == 83:
        print('x = ',x,'  y = ',y,'   z = ',z)
        print( x + y + z + 2 )


'''
Ответ
x =  12   y =  5    z =  9
28
'''
