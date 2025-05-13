print('x y z f') #НАЗВАНИЯ ПЕРЕМЕННЫХ И ФУНКЦИЯ
a=[True,False] #СПИСОК
for x in a:
    for y in a:
        for z in a:
            f=(not z) and x or x and y #ФУНКЦИЯ
            print(int(x), int(y), int(z), int(f))