#14.323
# Автор: А.Л. Наймушин
'''
Значение выражения 3•1158 + 15•1155 – 99•1118 + 125•119 + 381
записали в системе счисления с основанием 11. Сколько различных цифр
содержится в этой записи?
'''
x = 3*11**58 + 15*11**55 -99*11**18 + 125*11**9 + 381 

m = set()
s = ''
while (x != 0):
    s = str(x % 11)
    if s == '10': s = 'A'
    if s == '11': s = 'B'
    m.add(s)
    x = x // 11
  
print('n = ',len(m),';','  m = ', m )
'''
n =  7 ;   m =  {'0', '4', '1', '2', 'A', '7', '3'}
'''