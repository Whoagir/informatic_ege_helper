s=16**44*16**30-(32**5*(8**40-8**32)*(16**17-32**4))
s1=hex(s)[2:]
# print(s1)
s1=s1.replace('e','1')
# print(s1)
v=s1.count('1')
print(v)