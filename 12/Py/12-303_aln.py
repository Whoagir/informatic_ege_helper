
for x in range(0,50):
 for y in range(0,50):
  for z in range(0,50):
    s = "0" + '1'*x + '2'*y + '3'*z + '0'
    while '00' not in s:
      s = s.replace( '01', '21022', 1 )
      s = s.replace( '02', '310', 1 )
      s = s.replace( '03', '230112', 1 )
    if s.count('1') == 96 and s.count('2') == 36 and s.count('3') == 80:
      print( x + y + z + 2 )
      print ('x = ',x,'  y = ',y,'  z = ',z)

'''
Rez =
26
x =  6   y =  8   z =  10



'''

