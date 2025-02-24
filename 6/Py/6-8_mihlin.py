# Михлин Б.С.
'''
6.8 (В. Шубинкин) Исполнитель Чертёжник перемещается на координатной плоскости, оставляя след в виде линии.
Чертёжник может выполнять команду сместиться на (a, b), где a, b - целые числа.
Эта команда перемещает Чертёжника из точки с координатами (x, y) в точку с координатами (x + a; y + b).
    Например, если Чертёжник находится в точке с координатами (4, 2), то команда сместиться на (2, -3) 
    переместит Чертёжника в точку (6, -1).
Чертёжнику был дан для исполнения следующий алгоритм:
ПОВТОРИ 15 РАЗ
  сместиться на (10, 10)
  сместиться на (3, -6)
  сместиться на (-9, 3)
КОНЕЦ ПОВТОРИ
Определите, сколько точек с целочисленными координатами окажутся строго внутри замкнутых треугольных областей,
образованных линией, оставленной Чертёжником, если исполнитель стартует в точке с целочисленными координатами.
'''
def f(dx, dy, m):  # Черепашка выполняет команду Чертёжника "сместиться на (dx, dy)"
    x = xcor() + dx * m
    y = ycor() + dy * m
    goto(x, y)
    # return

from turtle import *
tracer(4)
screensize(5000, 5000)
width(2)
m = 20  # масштаб
pd()
# вручную считаем количество точек в треугольнике первого оборота цикла и
# умножаем на 15 (оборотов) 13 * 15 = 195 Ответ: 195
for i in range(1):
    f(10, 10, m)
    f(3, -6, m) # сместиться на (3, -6)
    f(-9, 3, m)
pu()
for x in range(0, 20):
    for y in range(0, 20):
        goto(x * m, y * m)
        dot('red')
done()
