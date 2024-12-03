# Автор В.Н. Шубинкин

with open('17-2.txt') as f:
    a = [int(x) for x in f.readlines()]

max_el = max(a)
print(a.count(max_el), a.index(max_el) + 1)

'''Рекомендую также ознакомиться с эффективным однопроходным алгоритмом
без использования методов массива и самого массива var2'''
