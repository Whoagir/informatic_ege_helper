# Автор В.Н. Шубинкин
from math import log

def get_sums(n: int) -> (int, int, int):
    digit_count = 0
    s = [0, 0]
    while n:
        digit_count += 1
        s[digit_count % 2] += n % 45
        n //= 45
    return min(s), max(s), digit_count

def alg(n: int) -> int:
    s_left, s_right, dc = get_sums(n)
    n += s_left * 45**dc
    len_s_rigth = int(log(s_right, 45)) + 1
    n = n * 45**len_s_rigth + s_right
    return n

r_min = 10**10
for n in range(1001, 1050):
    r = alg(n)
    r_min = min(r_min, r)
print('Ответ:', r_min)

#################################################
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
    n45 = from_dec(n, 45)
    s1 = sum([digits45.index(d) for d in n45[::2]])
    s0 = sum([digits45.index(d) for d in n45[1::2]])
    left = from_dec(min(s1, s0), 45)
    right = from_dec(max(s1, s0), 45)
    n45 = left + n45 + right
    return to_dec(n45, 45)

alphabet = digits + ascii_letters
digits45 = alphabet[:45]
r_min = 10**10
for n in range(1001, 100_000):
    r = alg(n)
    r_min = min(r_min, r)
print(r_min)
