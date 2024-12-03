// Автор: М. Нехорошева

#include<bits/stdc++.h>
using namespace std;
int main()
{
	int s=0,k=0,mx=0;
	fstream r;
	r.open("17-272.txt");
	vector <int> a;
	for(int x;r>>x;a.push_back(x));
	for(int i=0;i<a.size()-1;++i)
		if (a[i]>5024 or a[i+1]>5024)
		{
			++k;
			int	n=a[i],s=0;
			for(;n;s+=abs(n)%10,n/=10);
			int n1=a[i+1],s1=0;
			for(;n1;s1+=abs(n1)%10,n1/=10);
			mx=max(mx,max(s,s1));
		}
	cout << k << " " << mx;
}
