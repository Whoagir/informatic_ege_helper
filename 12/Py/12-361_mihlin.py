# Михлин Б.С.
'''
12.361 Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов. 
заменить(v, w) 
нашлось(v) 
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w.
Если цепочки v в строке нет, эта команда не изменяет строку.
Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор. 
Дана программа для Редактора:
ПОКА нашлось(01) ИЛИ нашлось(02)
  заменить(02, 1110)
  заменить(01, 2210)
КОНЕЦ ПОКА
На вход программе поступает строка длиной не менее 95 символов, первый из которых - цифра 0, а остальные – цифры 1 и 2.
После выполнения программы получилась строка, сумма цифр которой – степень числа 2.
Чему равна наименьшая возможная сумма цифр в исходной строке?
'''
r = []
for k1 in range(150):
    for k2 in range(150):
        if k1 + k2 >= 94:
            s = '0' + k1 * '1' + k2 * '2'   # исходная строка длиной не менее 95 символов
            while '01' in s or '02' in s:
                s = s.replace('02', '1110', 1).replace('01', '2210', 1)
            sm = sum(map(int, str(s)))      # сумма цифр полученной строки в десятичной системе
            # sm = s.count('1') + s.count('2') * 2
            if f'{sm:b}'.count('1') == 1:   # 2**n в двоичной системе имеет вид "10...0" (единица и n нулей)
            # if '1' not in f'{sm:b}'[1:]:
                r.append(k1 + k2 * 2)       # сумма цифр в исходной строке
print(min(r))  # Ответ: 108
