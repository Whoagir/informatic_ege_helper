// �����: �. ����������

//���� ������� (555) ��� ������� (888)
//  �������� (555, 8)
//  �������� (888, 55)
//����� ����

#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	string s1(101,'8'),s;
	for (;;s1+='8')
	{
		s=s1;
	for (;s.find("555")!=-1|| s.find("888")!=-1;)
	{	
		if(s.find("555")!=-1)
			s.replace(s.find("555"),3,"8");
		if(s.find("888")!=-1) 
			s.replace(s.find("888"),3,"55");
	}
		if (count(s.begin(),s.end(),'5')==0)
			{
				cout<<s1.size();
				break;
			}
	}
}
