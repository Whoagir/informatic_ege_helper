# ������ �.�.
'''
����� 123 �������� � �������� ��������� � ����������� �� 2 �� 10 ������������.
��� ����� ���������� ����� ����� ����� ��� ������ ����� �� ����� �������� ������������ �������������� ����������?
(����� ����������� � ���������� �������).
� ������ ������� ����� ���� ���������� ���������.
�����: 17
'''
s=0
for x in range(2,11):
    n=123
    nx=''
    while n:
        nx=str(n%x)+nx
        n//=x
    d=int(nx[1])-int(nx[0]) # ��� �������������� ����������
    if d<=0:
        continue
    for i in range(1,len(nx)-1):
        if int(nx[i+1])-int(nx[i])!=d:
            break
    else:
        s+=x
        #print(x,nx) # ����������
print(s) # �����: 17