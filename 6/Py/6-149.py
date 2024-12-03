from turtle import *
tracer(0)

lt(90)
pd()
lt(40)
for _ in range(5):
    rt(-95)
    fd(12*25)
    lt(45)
    fd(8*25)
    lt(40)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*25, y*25)
        dot(5)
update()
