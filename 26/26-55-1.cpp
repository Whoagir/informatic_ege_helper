// Автор: М. Нехорошева

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
int main()
{
	fstream f;
	f.open("26-55.txt");
	vector <int> a;
	int n,S,summa=0;
	f>>n>>S;
	for(int x;f>>x;a.push_back(x),summa+=x);
	sort(a.rbegin(),a.rend());
	int k=0,S1=S,x;
	for(;;)
	{
		x=0;
		for(int i =0;i<a.size();)
			if(S1-a[i]>=0)
				{
					x+=a[i];
					S1-=a[i];
					a.erase(a.begin()+i);
				}
			else
				++i;
		++k;
		summa-=x;
		S1=S;
		if (summa<=S)
		{
			++k;
			break;
		}
		
	}
	cout<<k<<"  "<<summa;
}

