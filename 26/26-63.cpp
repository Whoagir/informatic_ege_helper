// Автор: М. Нехорошева

#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	fstream F;
	F.open("26-62.txt");
	int N,S;
	F>>N>>S;
	int p;
	char c;
	vector<int>q,q1;
	vector<int> z;
	for(int i=0;i<N;++i)
	{
		F>>p;
		F>>c;
		if(c=='Z')
			z.push_back(p);
		if(c=='Q')
			q.push_back(p);				
	}
	sort(z.rbegin(),z.rend());
	sort(q.rbegin(),q.rend());
	int kz=0;
	for (;;)
		if (z.back()<=q.back())	
			{
				if (S<z.back())
					break;
				++kz;
				S-=z.back();
				z.pop_back();	
			}
		else
		{
			if (S<q.back())
					break;
			S-=q.back();
			q1.push_back(q.back());
			q.pop_back();		
		}
	for (;;)
		if (S+q1.back()>=z.back() && S>0)
		{	
			++kz;
			S=S+q1.back()-z.back();
			q1.pop_back();
			z.pop_back();
		}
		else break;
	cout<<kz<<"      "<<S;
}
