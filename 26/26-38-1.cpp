// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	fstream f;
	f.open("26-j9.txt");
	int S,n;
	vector <int> a;
	f>>S>>n;
	for(int x;f>>x;a.push_back(x));
	sort(a.begin(),a.end());
	int k=0,last;
	bool z=true;
	for (;;)
		if (z)
			{
			if (S-a.back()>=0)
				{
					++k;
					S-=a.back();
					last=a.back();
					a.pop_back();
					z=false;
				}
			else {
				a.pop_back();
				if(a.empty())
					break;
				}	
			}
		else
		{
			if (S-a.front()<0)
				break;
			++k;
			S-=a.front();
			last=a.front();
			a.erase(a.begin());
			z=true;
		}
	cout<<k<<"  "<<last;
}
