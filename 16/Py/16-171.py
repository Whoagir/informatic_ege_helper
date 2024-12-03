from math import ceil

a, b = 100000000, 200000000

# D = 105 = 3*5*7
s3, e3 = ceil(a / 3), int(b / 3)
s5, e5 = ceil(a / 5), int(b / 5)
s7, e7 = ceil(a / 7), int(b / 7)
s15, e15 = ceil(a / 15), int(b / 15)
s21, e21 = ceil(a / 21), int(b / 21)
s35, e35 = ceil(a / 35), int(b / 35)
s105, e105 = ceil(a / 105), int(b / 105)

wrong = e3 - s3 + 1 + e5 - s5 + 1 + e7 - s7 + 1 \
        - (e15 - s15 + 1) - (e21 - s21 + 1) - (e35 - s35 + 1) \
        + (e105 - s105 + 1)

print( b - a + 1 - wrong )

"""
from math import gcd
count = 0
for i in range(a, b+1):
  if gcd(i, 105) == 1:
    count += 1
print( count )
"""