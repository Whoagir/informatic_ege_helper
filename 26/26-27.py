# Автор: А.Н. Носкин
""" Идея:
считываем все числа в массив. Сортируем.
ищем значение медианы и среднее значение.
Считаем количество
"""
with open("26-j2.txt") as F:
  n = int(F.readline()) #

  a = [] # массив хранения всех чисел
  for i in range(n):
    monet = F.readline()  # очередное  число
    a.append(int(monet)) #  число добавили в массив

  a.sort()# сортировка по возрастанию
  mediana = a[n//2] # значение медианы
  sred = sum(a)/len(a)# среднее значение
  k = 0 #количество чисел
  for x in a:
    if sred <= x <= mediana or mediana <= x <= sred:
        k +=1
  print(k)



