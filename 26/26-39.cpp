// Автор: М. Нехорошева

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
int main()
{
	fstream f;
	f.open("26-39.txt");
	vector <int> d,d1,d2;
	int dd, n, x, k=0, s=0, a;
	f>>dd>>n;
	for (int i=0; i<n; ++i)
	{
		f>>x;
		if(x>179 && x<201)
			d.push_back(x);
		else d1.push_back(x);
	}
	sort (d.begin(), d.end());
	sort (d1.rbegin(), d1.rend());
	for (;;)
		if (dd-d.back()>=0 )
			{
				dd=dd-d.back();
				d.pop_back();
				++k;
			}
			else	
				break;		
	for (;;)
		if (dd-d1.back()>=0 )
			{
				dd=dd-d1.back();
				d1.pop_back();
				++k;
			}
			else	
				break;		

	cout<<k<<" ";
}
	
