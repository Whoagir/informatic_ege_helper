# ЕГЭ Задача № 14_242. Михлин Б.С.
a=int('0o46',8)
b=int('0x40',16)
c=int('0o47',8)-int('0x1B',16)
d=int('0b110101',2)+int('0o13',8)
print(a,b,c,d)
x=3*16**a+5*4**b-8**c-2**d+15
x16=hex(x)
print(x)
print(x16)
print('Ответ:',x16.count('f'))
'''
38 64 12 64
17126974013883353177391748931820234653004988431
0x3000004fffffffffffffffefffffff00000000f
Ответ: 23
'''
