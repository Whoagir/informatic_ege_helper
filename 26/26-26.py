# Автор: А.Н. Носкин
""" Идея:
считываем все кол-во монет из корзин в массив.
Перебираем все возможнные пары корзин. Если сумма монет
из двух корзин = 100, то они становятся пустые, т.е. равны 0.
Это можно сделать присвиванием 0 двум корзинам или a[j]=0 и break
"""
with open("26-j1.txt") as F:
  n = int(F.readline()) #

  a = [] # массив хранения всех монет
  for i in range(n):
    monet = F.readline()  # очередная корзина с монетами
    a.append(int(monet)) #  число добавили в массив

  k = 0 #количество ящиков, заполненными 100 монетами
  for i in range(n-1):
    for j in range(i+1,n):
      if a[i]+a[j] == 100:
        k +=1
        a[j] = 0 # корзину №2 высыпали в ящик
        #break - корзину №1 учли или можно обнулить a[i]
        a[i] = 0
  print(k)


