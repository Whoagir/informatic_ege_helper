// Автор: М. Нехорошева

//НАЧАЛО
//  ПОКА нашлось (68) ИЛИ нашлось (7777)
//    заменить (68, 7)
//    заменить (7777, 7)
//  КОНЕЦ ПОКА
//КОНЕЦ
#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
	string s="";
	for (int i=0;i<144;s=s+"687",++i);
	for(;s.find("68")!=-1 || s.find("7777")!=-1;)
	{
		if(s.find("68")!=-1)
			s.replace(s.find("68"),2,"7");
		if (s.find("7777")!=-1)
			s.replace(s.find("7777"),4,"7");
	}
	cout<<s;	
}
