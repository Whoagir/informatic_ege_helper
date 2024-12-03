// Автор: М. Нехорошева

#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
	int m=0;string s(138,'1');
	for(int i=138;i<2000;s+="1",++i)
	{
		for (;s.find("111")!=-1;)
		{
			if (s.find("111")!=-1)
				s.replace(s.find("111"),3,"2");
			if (s.find("2222")!=-1)
				s.replace(s.find("2222"),4,"1");
		}
		int  k=0;
		for (int j=0;j<s.size();++j)
			if (s[j]=='1')
				++k;
		m=max(m,k);
	}
	cout<<m;
}
