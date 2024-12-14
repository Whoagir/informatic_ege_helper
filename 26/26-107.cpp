// Автор: М. Нехорошева

#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
	fstream F;
	F.open("26-107.txt");
	vector<pair<int,int> >a;
	int n,L;
	F>>L>>n;
	for (int x,y;F>>x>>y;a.emplace_back(y,x));
	sort(a.begin(),a.end());
	int k=1,last=a[0].first,time_last;
	for (int i=1;i<a.size();++i)
		if (a[i].second>=last)
			++k,last=a[i].first,time_last=a[i].second;
	cout<<k<<"  "<<	time_last;
}
