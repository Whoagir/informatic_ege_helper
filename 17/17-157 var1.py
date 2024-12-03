# Автор В.Н. Шубинкин

with open('17-2.txt') as f:
    a = [int(x) for x in f.readlines()]

min_el = min(a)
print(a.count(min_el), len(a) - a[::-1].index(min_el))

'''Рекомендую также ознакомиться с эффективным однопроходным алгоритмом
без использования методов массива и самого массива var2'''
