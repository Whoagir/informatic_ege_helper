"""
Р-11 (демо-2021).

Игорь составляет таблицу кодовых слов для передачи сообщений, каждому
сообщению соответствует своё кодовое слово. В качестве кодовых слов
Игорь использует трёхбуквенные слова, в которых могут быть только буквы
Ш, К, О, Л, А, причём буква К появляется ровно 1 раз. Каждая из других
допустимых букв может встречаться в кодовом слове любое количество раз
или не встречаться совсем. Сколько различных кодовых слов может
использовать Игорь?

"""

from itertools import product

p = product('ШКОЛА',repeat=3)

n = 0
for x in p:
    if x.count('К') == 1:
        n += 1
print(n)

# ---------------------------------------------------------------------
"""
Р-09.  Маша составляет 5-буквенные коды из букв В, У, А, Л, Ь.
Каждую букву нужно использовать ровно 1 раз,
при этом код буква Ь не может стоять на первом месте и перед гласной.
Сколько различных кодов может составить Маша?
"""

from itertools import product

p = product('ВУАЛЬ',repeat=5)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
   if ((x.count('В')==1) and (x.count('У')==1) and (x.count('А')==1) and (x.count('Л')==1) and (x.count('Ь')==1))\
    and (x[0] != 'Ь') and (x.find('ЬУ')==-1 and x.find('ЬА')==-1):
        n += 1
print(n)

# ---------------------------------------------------------------------
"""
Р-08.  Вася составляет 4-буквенные коды из букв У, Л, Е, Й.
Каждую букву нужно использовать ровно 1 раз,
при этом код не может начинаться с буквы Й и не может содержать сочетания ЕУ.
Сколько различных кодов может составить Вася?

"""
from itertools import product

p = product('УЛЕЙ',repeat=4)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if (x.count('У') == 1) and (x.count('Л') == 1) and (x.count('Е') == 1) and (x.count('Й') == 1)\
    and (x[0] != 'Й') and (x.find('ЕУ')==-1):
        n += 1
print(n)

# -------------------------------------------------------------------------
"""
Р-07.  Вася составляет 3-буквенные слова, в которых есть только буквы В, Е, С, Н , А,
причём буква А используется в каждом слове хотя бы 1 раз.
Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?

"""
from itertools import product

p = product('ВЕСНА',repeat=3)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if (x.count('А') >= 1):
        n += 1
print(n)

# --------------------------------------------------------------------------
"""
Р-06. Вася составляет 5-буквенные слова, в которых есть только буквы С, Л, О, Н,
причём буква С используется в каждом слове ровно 1 раз.
Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?
"""
from itertools import product

p = product('СЛОН',repeat=5)

n = 0
for x in p:
    if x.count('С') == 1:
        n += 1
print(n)

# --------------------------------------------------------------------------
"""
Р-05. Сколько существует различных символьных последовательностей длины 5 в четырёхбуквенном алфавите {A, C, G, T},
которые содержат ровно две буквы A?
"""
from itertools import product

p = product('ACGT',repeat=5)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if (x.count('A') == 2):
        n += 1
print(n)

# -----------------------------------------------------------------------

"""
Р-04. Сколько слов длины 5, начинающихся с гласной буквы, можно составить из букв Е, Г, Э?
Каждая буква может входить в слово несколько раз.
Слова не обязательно должны быть осмысленными словами русского языка.
"""
from itertools import product

p = product('ЕГЭ',repeat=5)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if (x[0] == 'Е') or (x[0] == 'Э'):
        n += 1
print(n)

# -------------------------------------------------------------------------

"""
26)	Сколько слов длины 5, начинающихся с согласной буквы и заканчивающихся гласной буквой,
можно составить из букв К, У, М, А?
Каждая буква может входить в слово несколько раз.
Слова не обязательно должны быть осмысленными словами русского языка.
"""
from itertools import product

p = product('КУМА',repeat=5)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if ((x[0] == 'К') or (x[0] == 'М')) and ((x[4] == 'У') or (x[4] == 'А')) :
        n += 1
print(n)

# ------------------------------------------------------------------------

"""
31)	Сколько слов длины 4, начинающихся с согласной буквы и заканчивающихся гласной буквой,
можно составить из букв М, Е, Т, Р, О?
Каждая буква может входить в слово несколько раз.
Слова не обязательно должны быть осмысленными словами русского языка.
"""

from itertools import product

p = product('МЕТРО',repeat=4)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if ((x[0] == 'М') or (x[0] == 'Т') or (x[0] == 'Р')) and ((x[3] == 'Е') or (x[3] == 'О')) :
        n += 1
print(n)

# ------------------------------------------------------------------------
"""
32)	(Е.В. Хламов) Сколько существует различных символьных последовательностей
длины 3 в четырёхбуквенном алфавите {A,B,C,D},
если известно, что одним из соседей A обязательно является D,
а буквы B и C никогда не соседствуют друг с другом?
"""
from itertools import product

p = product('ABCD',repeat=3)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if x.find('A')>=0:
        if ((x.find('AD')>=0) or (x.find('DA')>=0)) and ((x.find('AA')==-1)) and ((x.find('BC')==-1) or (x.find('CB')==-1)):
            n += 1

    if (x.find('A')==-1):
        if (x.find('B')>=0) and (x.find('C')>=0):
            if ((x.find('BC')==-1) and (x.find('CB')==-1)):
                n += 1

        if ((x.find('B')>=0) and (x.find('C')==-1)) or ((x.find('B')==-1) and (x.find('C')>=0))\
        or ((x.find('B')==-1) and (x.find('C')==-1)):
            n += 1
print(n)

# -------------------------------------------------------------------------------------------------

"""
40)	Алексей составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
В качестве кодовых слов Алексей использует 5-буквенные слова, в которых есть только буквы A, B, C, X,
причём буква X может появиться на последнем месте или не появиться вовсе.
Сколько различных кодовых слов может использовать Алексей?
"""

from itertools import product

p = product('ABCX',repeat=5)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if ((x[4] == 'X') and (x.count('X')==1)) or ((x.find('X')==-1)):
            n += 1
print(n)

# ------------------------------------------------------------------------------------------------

"""
50)	Вася составляет 4-буквенные слова, в которых есть только буквы К, А, Т, Е, Р,
причём буква Р используется в каждом слове хотя бы 2 раза.
Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?
"""

from itertools import product

p = product('КАТЕР',repeat=4)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if (x.count('Р')>=2):
            n += 1
print(n)

# ------------------------------------------------------------------------------------------------
"""
56)	(М.В. Кузнецова) Вася составляет 5-буквенные слова, в которых есть только буквы С, И, Р, О, П,
причём в каждом слове обязательно есть ровно одна буква О, при этом стоять она может только после согласной.
Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?

"""
from itertools import product

p = product('СИРОП',repeat=5)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if ((x.count('О')==1) and ((x.find('СО')>=0) or (x.find('РО')>=0) or (x.find('ПО')>=0))):
            n += 1
print(n)

# -----------------------------------------------------------------------------------------------------

"""
69)	Олег составляет таблицу кодовых слов для передачи сообщений,
каждому сообщению соответствует своё кодовое слово.
В качестве кодовых слов Олег использует 4-буквенные слова,
в которых есть только буквы A, Б, В, Г, Д и Е, причём буква Г появляется ровно 1 раз
и только на первом или последнем месте.
Каждая из других допустимых букв может встречаться в кодовом слове любое количество раз или не встречаться совсем.
Сколько различных кодовых слов может использовать Олег?
"""

from itertools import product

p = product('АБВГДЕ',repeat=4)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
   if ((x[0] == 'Г') and (x.count('Г')==1)) or ((x[3] == 'Г') and (x.count('Г')==1)):
        n += 1
print(n)

# ----------------------------------------------------------------------------------------------------

"""
91)	Вася составляет 5-буквенные коды из букв К, А, Л, И, Й.
Каждую букву нужно использовать ровно 1 раз,
при этом код не может начинаться с буквы Й и не может содержать сочетания ИА.
Сколько различных кодов может составить Вася?
"""

from itertools import product

p = product('КАЛИЙ',repeat=5)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
   if ((x.count('К')==1) and (x.count('А')==1) and (x.count('Л')==1) and (x.count('И')==1) and (x.count('Й')==1))\
    and (x[0] != 'Й') and (x.find('ИА')==-1):
        n += 1
print(n)

# ---------------------------------------------------------------------------------------------------

"""
110)	Маша составляет 6-буквенные коды из букв Р, У, Л, Ь, К, А.
Каждую букву нужно использовать ровно 1 раз,
при этом код буква Ь не может стоять на первом месте и после гласной.
Сколько различных кодов может составить Маша?
"""
from itertools import product

p = product('РУЛЬКА',repeat=6)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
   if ((x.count('Р')==1) and (x.count('У')==1) and (x.count('Л')==1) and (x.count('Ь')==1) and (x.count('К')==1) and (x.count('А')==1))\
    and (x[0] != 'Ь') and (x.find('УЬ')==-1) and (x.find('АЬ')==-1):
        n += 1
print(n)

# -----------------------------------------------------------------------------------------------------
"""
120)	(А.М. Кабанов) Юрий составляет 4-буквенные слова из букв П, Р, И, К, А, З.
Каждую букву можно использовать не более одного раза, при этом в слове нельзя использовать более одной гласной.
Сколько различных кодов может составить Юрий?
"""

from itertools import product

p = product('ПРИКАЗ',repeat=4)
s = map(lambda x: ''.join(x), p)

n = 0
for x in s:
    if ((x[0] != x[1]) and (x[0] != x[2]) and (x[0] != x[3])and (x[1] != x[2]) and (x[1] != x[3]) and (x[2] != x[3]))\
    and (((x.count('И')==1) and (x.count('А')==0)) or ((x.count('И')==0)and (x.count('А')==1)) or ((x.count('И')==0) and (x.count('А')==0))):
        n += 1
print(n)

# ------------------------------------------------------------------------------------------------------
