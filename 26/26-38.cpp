// Автор: М. Нехорошева

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
int main()
{
	fstream f;
	f.open("26-j9.txt");
	vector <int> d;
	int dd, n, x, k=0, s=0, a, b;
	f>>dd>>n;
	bool z=true;
	for (int i=0; i<n; ++i)
	{
		f>>x;
		d.push_back(x);
	}
	sort (d.begin(), d.end());
	for (;;)
	{
		if(z)
			if (dd-d.back()>=0)
			{
				dd=dd-d.back();
				a=d.back();
				d.pop_back();
				++k;
				z=false;
			}
			else	
					d.pop_back();
		else
		
			if (dd-d.front()>=0)
			{
				dd=dd-d.front();
				++k;
				a=d.front();
				d.erase(d.begin());
				z=true;
			}
		if (d.empty() || dd-d.front()<0 && dd-d.back()<0)
			break;
	}

	cout<<k<<" "<<a;
}
	
