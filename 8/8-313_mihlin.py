'''
8.313 (C. ������) ������� ���������� �����, ����������� ����� � ����� ����������.
������� ��������� ����, � ������� ����, ���� ��, 2 ������ ������ ������� ����� ��������� �������?
'''
from itertools import *
r={x for x in permutations('����������') if any(x[i] in '��' and x[i+1] in '��' for i in range(9))}
print(len(r)) # 756000 # ������� ��������� ����, ...
#r=[x for x in permutations('����������') if any(x[i] in '��' and x[i+1] in '��' for i in range(9))]
#print(len(r)) # 3024000 