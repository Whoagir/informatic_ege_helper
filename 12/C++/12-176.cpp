// Автор: М. Нехорошева

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{  
	string s="";
	for (int  i=0;i<200;++i)
		s=s+"5";
	for(;s.find("555")!=-1 || s.find("333")!=-1;)
		if (s.find("555")!=-1)
			s.replace(s.find("555"),3,"3");
		else 
			s.replace(s.find("333"),3,"5");

    cout<<s;
	cout<<count(begin(s), end(s), '3'); 
return 0;
}
