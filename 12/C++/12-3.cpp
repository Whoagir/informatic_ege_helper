// Автор: М. Нехорошева

#include <iostream>
#include <string>
using namespace std;
int main()
{  

 string s="";
for (int  i=0;i<2019;++i)
	s="1"+s+"3";

for (;s.find("111")!=-1;)
   {
   		if(s.find("111")!=-1) s.replace(s.find("111"),3,"2");
   		if(s.find("222")!=-1) s.replace(s.find("222"),3,"3");
   		if(s.find("333")!=-1) s.replace(s.find("333"),3,"1");cout<<s<<endl;
    }
    

return 0;
}
