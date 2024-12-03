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
	F.open("17-298.txt");
	vector<int> a;
	for (int x;F>>x;a.push_back(x));
	int k=0,m197=0,sm=0;
	for (int i=0;i<a.size();++i)
		if (a[i]%197==0) 
			m197=max(m197,a[i]);
	for (int i=0;i<a.size()-1;++i)
	{
		bool f1=(a[i]==197 || a[i]==985 ||a[i]==1379);
		bool f2=(a[i+1]==197 || a[i+1]==985 ||a[i+1]==1379);
		if (f1^f2 && a[i]+a[i+1] <m197)
			++k, sm=max(sm,a[i]+a[i+1]);
	}			
	
	cout<<k<<" "<<sm;
}
