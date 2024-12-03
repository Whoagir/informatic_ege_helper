from math import ceil

a, b = 100000000, 200000000

# D = 21 = 3*7
s3, e3 = ceil(a / 3), int(b / 3)
s7, e7 = ceil(a / 7), int(b / 7)
s21, e21 = ceil(a / 21), int(b / 21)

wrong = e3 - s3 + 1 + e7 - s7 + 1 - (e21 - s21 + 1)

print( b - a + 1 - wrong )
