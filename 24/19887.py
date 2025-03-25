import re

f=open('24.23_19887.txt')
a=f.read()
pattern1=r'(?:[02468][13579])*'
pattern2=r'(?:[13579][02468])*'
s=re.findall(pattern1,a)
s1=re.findall(pattern2,a)
print(max([len(i) for i in s]),max([len(i) for i in s1]))