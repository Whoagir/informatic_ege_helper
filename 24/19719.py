import re
f=open('24.12_19719.txt')
a=f.read()
pattern=r'(?:0|[1-9][0-9]*)(?:[*-](?:0|[1-9][0-9]*))*'
matches=re.findall(pattern,a)
print(matches)
print(max([len(i) for i in matches]))
