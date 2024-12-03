# Автор: А. Носкин

from turtle import *
k = 30 # масштаб
left(90)
for i in range(15):
    forward( k*4 )
    right(60)

up()
for x in range(0, 8):
  for y in range(0, 8):
    goto(x*k, y*k)
    dot(4)

