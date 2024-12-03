// Автор: М. Нехорошева

#include <iostream>
#include <string>
using namespace std;
int main()
{  

 string s="1";
for (int  i=0;i<80;++i)
	s+="0";

   for (;s.find("10")!=-1 or s.find("1")!=-1;)
   {
	   if(s.find("10")!=-1)
   		s.replace(s.find("10"),2,"001");
 	else
	 {
	 	s.replace(s.find("1"),1,"000");
   		}
   }
    cout<<s.size();

return 0;
}
