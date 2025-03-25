from functions import ctb
s=5*216**1156-4*36**1147+6**1153-875
s1=ctb(s,6)
print(s1.count('5')-s1.count('0'))