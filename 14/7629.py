from functions import ctb
for x in range (2031,1,-1):
    s=7**170+7**100-x
    s1=ctb(s,7)
    if s1.count('0')==71:
        print(x)
        break