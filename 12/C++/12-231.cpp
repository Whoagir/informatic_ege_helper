// Автор: М. Нехорошева

#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
	for (int n=1;n<20;++n)
	{
		string s="3232323232323232";
		for (int i=0;i<n;s="3"+s,++i);
		cout<<s<<endl;
		for(;s.find("32")!=-1 ;)
			if(s.find("32")!=-1)
				s.replace(s.find("32"),2,"6");
		int k=count(s.begin(),s.end(),'2')*2 + count(s.begin(),s.end(),'3')*3 + count(s.begin(),s.end(),'6')*6;
		cout<<s<<"  "<<k<<endl;
		if (k==93)
		{
			cout<<n+8;
			break;
		}
	}
	
}
