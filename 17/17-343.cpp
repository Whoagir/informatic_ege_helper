// Автор: М. Нехорошева

#include<bits/stdc++.h>
using namespace std;
int f(int x, int s, int q)
{
	for (int j=0;x;++j, x/=10)
	{
		if (j%2==q)
		s+=abs(x)%10;
	}
	return s;
}
int main()
{
	int k=0,mn=100000;
	vector <int> a;
	fstream r;
	r.open("17-343.txt");
	for (int x;r>>x;a.push_back(x));
	for (int i=0;i<a.size()-2;++i)
	{
		int c1=f(a[i],0,0), c2=f(a[i+1],0,0), c3=f(a[i+2],0,0);
		if (c1!=0 and c2!=0 and c3!=0)
		{
			if (f(a[i],0,1)%c1==0 and f(a[i+1],0,1)%c2==0 and f(a[i+2],0,1)%c3==0)
			{
				k++;
				if (a[i]+a[i+1]+a[i+2] < mn)
					mn=(a[i]+a[i+1]+a[i+2]);
			}
		}
	}
		cout << k << " " << mn;
}
