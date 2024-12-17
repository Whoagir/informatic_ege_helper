def is_pal(s: str) -> bool:
    return s == s[::-1]


c = 0
for n in range(100, 200):
    s = str(n)
    n1 = int(s) + int(s[::-1])
    s1 = str(n1)
    n2 = int(s1) + int(s1[::-1])
    s2 = str(n2)
    n3 = int(s2) + int(s2[::-1])
    s3 = str(n3)
    n4 = int(s3) + int(s3[::-1])
    s4 = str(n4)
    n5 = int(s4) + int(s4[::-1])
    s5 = str(n5)
    n6 = int(s5) + int(s5[::-1])
    s6 = str(n6)
    if is_pal(s1) or is_pal(s2) or is_pal(s3) or is_pal(s4) or is_pal(s5) or is_pal(s6):
        c += 1
print(c)
