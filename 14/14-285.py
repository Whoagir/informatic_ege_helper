# ������ �.�.
'''
����� 437 �������� � �������� ��������� � ����������� �� 2 �� 10 ������������.
��� ����� ���������� ����� ���� ����� ����� �������� ������� ������?
(����� ����������� � ���������� �������. ����� ���������� �������, ���� ����� ������ 2 ��������: ������� ������ ������ �� 1 � �� ������ ����).
� ������ ������� ����� ���� ���������� ���������.
�����: 33
'''
sdx=[0]*11  # ������ ���� ���� ����� � ������� �����������
s=0         # ����� ���������� ���������
for x in range(2,11):
    n=437   # ����� � ���������� �������
    nx=''   # ��������� ������ ����� � ���������� x
    while n:
        nx=str(n%x)+nx
        n//=x
    dx=[int(d) for d in nx] # ������ ���� ����� � ���������� x
    sdx[x]=sum(dx) # ������ ����� ���� ����� � ���������� x  
#print(sdx) # ����������
for x in range(2,11):
    for de in range(2,sdx[x]): # ������� ���������
        if sdx[x]%de==0:
            break
    else:
        s+=x
        #print(x,sdx[x]) # ����������
print(s) # �����: 33