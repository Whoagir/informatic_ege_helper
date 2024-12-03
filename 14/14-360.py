# Автор В.Н. Шубинкин

from string import digits as d, ascii_uppercase as letters
digits = d + letters

def f(a):
    for x in range(15):
        for y in range(13):
            if x >= 13:
                break
            x1 = f'2{digits[y]}23{digits[x]}5'
            x2 = '67' + digits[x] + '9' + digits[y]
            if (int(x1, 15) + a) % int(x2, 13) == 0:
                return True
    return False


a = 1
while not f(a):
    a += 1
print(a)

