# Автор: Н. Гаязова

X,Y,Z = ord('X')-55, ord('Y')-55, ord('Z')-55
n = []
for a in range(0,54+1):
    n1 = Z*(55**3)+a*(55**2)+Y*(55**1)+X*(55**0)
    n2 = 2*(55**3)+X*(55**2)+a*(55**1)+Y*(55**0)
    if (n1-n2)%29==0:
        n+=[n1-n2]
print( abs(n[0]-n[-1]) )

# Ответ: 86130

