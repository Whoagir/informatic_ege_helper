# Михлин Б.С. 1-й способ решения
'''
5.300 (Е. Джобс) На вход алгоритма подаётся натуральное число N > 1.
Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. Из полученной записи убирается старшая (левая) единица.
3. Если в полученной записи количество единиц четное, то слева дописывается 10, иначе слева дописывается 1, а справа - 0.
Полученная таким образом запись является двоичной записью искомого числа R.
Например, для исходного числа 4(10) = 100(2) результатом будет являться число 8(10) = 1000(2),
а для исходного числа 6(10) = 110(2) результатом будет являться число 12(10) = 1100(2).
Укажите максимальное десятичное число R, меньшее 450, которое может являться результатом работы алгоритма.
В ответе запишите это число в десятичной системе счисления.
'''
rma = 0  # максимальное значение r
for n in range(2, 10_000):
    r = f'{n:b}'[1:]    # 1, 2 (f-строка и срез)
    r = '10' + r if r.count('1') % 2 == 0 else '1' + r + '0'  # 3 (тернарная форма if)
    r = int(r, 2)       # перевод r из 2-ой в 10-ую систему
    if rma < r < 450:
        rma = r
print(rma)              # Ответ: 444