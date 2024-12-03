# Автор В.Н. Шубинкин


def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(5 * y + 7 * x != 129 or 3 * x > a or 4 * y > a):
                return False
    return True


a = 1000
while not f(a):
    a -= 1
print(a)
