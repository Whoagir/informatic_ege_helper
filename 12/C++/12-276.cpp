// Автор: М. Нехорошева

#include <iostream>
using namespace std;
int main()
{  
	int k=101;
	string s1="",s;
	for (int  i=0;i<k;++i)
			s1+="5";
	s="8";
	for (;s.find("8")!=-1;k++,s1+="5")
	{
		s=s1;
		for (;s.find("555")!=-1 or s.find("888")!=-1;)
	   		{
	   			if(s.find("555")!=-1)
   					s.replace(s.find("555"),3,"8");
  				if(s.find("888")!=-1)
	 				s.replace(s.find("888"),3,"55");	
	   		}
	   	cout<<k<<" "<<s<<endl;	
	}
	cout<<k-1;
	return 0;
}
