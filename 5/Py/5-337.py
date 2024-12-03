# Автор В.Н. Шубинкин

def get_sums(n: int) -> [int, int]:
    s = [0, 0]
    while n:
        s[n % 2] += n % 80
        n //= 80
    return s

def alg(n: int) -> int:
    s = get_sums(n)
    add_digit = max(s) % 80
    n = n * 80 + add_digit
    s[add_digit % 2] += add_digit
    add_digit = max(s) % 80
    n = n * 80 + add_digit
    return n

n = 1
while alg(n) <= 10**6:
    n += 1
print(f'N = {n}, R = {alg(n)}')
print(f'Ответ: {n}')

###############################################
# Вариант 2
# Автор В.Н. Шубинкин

from string import digits, ascii_letters

def from_dec(n: int, base: int) -> str:
    result = ''
    while n:
        result = alphabet[n % base] + result
        n //= base
    return result

def to_dec(s: str, base: int) -> int:
    result = 0
    base_power = 1
    for d in s[::-1]:
        result += alphabet.index(d) * base_power
        base_power *= base
    return result

def alg(n: int) -> int:
    n80 = from_dec(n, 80)
    for _ in range(2):
        s = [0, 0]
        for d in n80:
            s[d not in even_digits] += digits80.index(d)
        n80 += digits80[max(s) % 80]
    return to_dec(n80, 80)    

alphabet = digits + ascii_letters + 'йцукенгшщзхъфывапролджэячсмитьбю'
digits80 = alphabet[:80]
even_digits = digits80[::2]
n = 1
while alg(n) <= 10**6:
    n += 1
print(f'N = {n}, R = {alg(n)}')
print(f'Ответ: {n}')
# Ответ: 156
