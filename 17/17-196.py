"""
Автор задачи и решения: Л. Шастин
В файле 17-10.txt содержится последовательность целых чисел. Элементы последовательности могут принимать значения от 0 до 10000 включительно.
Определите сначала количество троек элементов последовательности, ив которых можно составить прямоугольный треугольник, а затем сумму всех
гипотенуз треугольника в подходящих тройках. Под тройкой подразумевается три идущих подряд элемента последовательности.
"""
def filtration(troyka):
  mas = sorted([troyka[0],troyka[1],troyka[2]])
  return ((mas[0]**2)+(mas[1]**2) == (mas[2]**2) and
          (mas[0]+mas[1]) > mas[2] and (mas[0]+mas[2]) > mas[1]
           and (mas[1]+mas[2]) > mas[0])
s = 0
numbers = list(map(int, open('17-10.txt').readlines()))
troyki = tuple(filter(filtration, zip(numbers, numbers[1:],numbers[2:])))
for el in range(len(list(troyki))):
  s += max(troyki[el][0], troyki[el][1],troyki[el][2])
print( len(troyki), s )

# ИЛИ
elems = list(map(int, open('17-10.txt').readlines()))
k = s = 0
for el in range(len(elems)-2):
  x, y, z = elems[el], elems[el+1], elems[el+2]
  if ((((x**2)+(y**2)) == (z**2)) or (((x**2)+(z**2)) == (y**2)) or ((y**2)+(z**2)) == (x**2)):
    k += 1
    s += max(x,y,z)
print( k, s )
