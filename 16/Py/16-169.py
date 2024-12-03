from math import ceil

a, b = 100000000, 200000000

# D = 15 = 3*5
s3, e3 = ceil(a / 3), int(b / 3)
s5, e5 = ceil(a / 5), int(b / 5)
s15, e15 = ceil(a / 15), int(b / 15)

wrong = e3 - s3 + 1 + e5 - s5 + 1 - (e15 - s15 + 1)

print( b - a + 1 - wrong )
