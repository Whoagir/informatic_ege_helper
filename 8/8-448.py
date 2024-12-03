from itertools import product

A = "АБВЕОПРС"
count = 0
for w1 in product(A, repeat=3):
  w1 = ''.join(w1)
  for w2 in product(A, repeat=3):
    w2 = ''.join(w2)
    if w1 != w2: count += 1
print( 2*count )

# Автор: Д. Шамсутдинов

from itertools import *
c=0
for s in product('АБВПРСОЕ',repeat=3):
    s=''.join(s) #образуем первый корень длиной 3
    for s2 in product('АБВПРСОЕ',repeat=3):
        s2=''.join(s2) #образуем второй корень длиной 3
        if s!=s2: c+=1 #проверяем, чтобы корни не совпали и прибавляем счётчик
print(c*2) #увеличиваем количество в 2 раза, так как у нас две соединительных гласных

from itertools import *
c=0
for s in product('АБВЕОПРС',repeat=7):
    s=''.join(s) #образуем слово длиной 7
    if s[3]=='О' or s[3]=='Е': #проверка на то, что четвёртая буква является соединительной гласной
        if s[0:3]!=s[4:8]: #проверяем, что корни не совпадают
            c+=1 #увеличение счётчика на 1
print(c)
