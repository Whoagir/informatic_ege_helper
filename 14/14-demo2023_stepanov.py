# Автор: И. Степанов

print('-----------Demo1-----------------')
for x in '0123456789ABCDE':
    a = int('123'+x+'5', 15) + int('1'+x+'233', 15)
    if a % 14 == 0:
        print('x =', x,'Otvet:', a//14)
        break

print('-----------Demo2-----------------')

def perevod(s,c,x):
    a = 0
    for i in range(len(s)):
        if s[i] != 'x':
            a += int(s[i],c) * c**i
        else:
            a+= x * c**i
    return a

dig =[i for i in range(15)]
for x in dig:
    s1='123x5'[::-1]
    s2='1x233'[::-1]
    a = perevod(s1,15,x) + perevod(s2,15,x)
    if a % 14 == 0:
        print('x =', x,'Otvet:', a//14)
        break




