from functions import *
for x in range(1,2031):
    s=6**260+6**160+6**60-x
    s1=ctb(s,6)
    if s1.count('0')==202:
        print(x)