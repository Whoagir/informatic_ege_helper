// �����: �. ����������

/*���������� � �������� � ������ ������� ���������� ��� ��������� ������������������, � ������� ���� �� 
���� ����� ������� �� 7, � ������ ��� ���� �� ������� �� 17. 
����� - ����������� �� ���� ��������� ����� ���. */
#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
	fstream Fin;  //��������� ���� � ������ ������  
	Fin.open("17-1.txt");
	int a,s_min=1000000, k=0;
	Fin>>a;
	for(int b;Fin>>b;)
	{
		if((a%7==0 && b%17!=0) || (b%7==0 && a%17!=0))
		{
			++k;
			if (a+b<s_min)
				s_min=a+b;
		}
		a=b;
	}
	cout<<k<<" "<<s_min;
}
