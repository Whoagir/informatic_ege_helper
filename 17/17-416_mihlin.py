'''
17.416 (�. ����������) � ����� 17-411.txt ���������� ������������������ ����������� �����, �� ����������� (1000?) 1150.
���������� ���������� �������� ��������� ������������������, � ������� ���������� ������ ��������� ������� �
��� ������ �������� ������ ������������� ��������, ��������������� �� 1. � ������ �������� ���������� ��������� ��������,
����� ����������� �� ���� ��������� ����� ��������.
� ������ ������ ��� ��������� ��������������� ������ ������ ������ �������� ������������������.
'''
m=[int(x) for x in open('17-411.txt')]
#print(max(m))                    # 1150 !!
ma=max([x for x in m if x%10==1]) # 1081 !!
r=[]
for i in range(len(m)-3):
    a,b,c,d=m[i:i+4]
    #if ((a%2==0 and a<ma)+(b%2==0 and b<ma)+(c%2==0 and c<ma)+(d%2==0 and d<ma))%2!=0: # 125 559 !!
    if ((a%2==0)+(b%2==0)+(c%2==0)+(d%2==0))%2 and all(x<ma for x in (a,b,c,d)):        # 117 559 ������ �����    
        r+=[a+b+c+d]
print(len(r),min(r)) # 117 559