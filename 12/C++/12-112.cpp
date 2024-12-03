// Автор: М. Нехорошева

#include <iostream>
#include <string>
using namespace std;
int main()
{  
	string s="";
	for (int  i=0;i<;++i)
		s=s+"8";
	for(;s.find("222")!=-1 || s.find("888")!=-1;)
		if (s.find("222")!=-1)
			s.replace(s.find("222"),3,"8");
		else 
			s.replace(s.find("888"),3,"2");

    cout<<s;

return 0;
}
