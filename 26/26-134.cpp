// Автор: М. Нехорошева

#include<bits/stdc++.h>
using namespace std;
int main()
{
	fstream f;
	f.open("26-134.txt");
	vector <pair<int,int> > G,W,M;
	int t=0,kg=0,kw=0,km=0,vremya=0,n=0,k;
	f>>k>>t;
	char z;
	for (int i=0,x,y ; i<k ; i++)
		{
		f >> x >> y >> z;
		if (z=='G')
			G.emplace_back(x,y);
		if (z=='W')
			W.emplace_back(x,y);
		if (z=='M')
			M.emplace_back(x,y);
		}
	sort(G.begin(),G.end());
	sort(W.begin(),W.end());
	sort(M.begin(),M.end());
	char people;

	for (;;)
		{
			int	r=min(G[0].first,min(W[0].first,M[0].first));
			if (vremya<r)
				vremya=r;
			if (G[0].first<=vremya)
			{
				vremya+=G[0].second;
				++kg;
				n++;
				people='G';
				G.erase(G.begin());
			}
			else 
				if (W[0].first<=vremya)
				{
					vremya+=W[0].second;
					++kw;
					n++;
					people='W';
					W.erase(W.begin());
				}
				else 
					if (M[0].first<=vremya)
					{
						vremya+=M[0].second;
						++km;
						n++;
						people='M';
						M.erase(M.begin());
					}
	
			if (vremya>=t) break;
	}
	cout << n << " " << people << endl;
	cout << kg << " " << kw << " " << km;
}
