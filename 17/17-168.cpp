// Автор: М. Нехорошева

#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
int main()
{
	fstream F;
	F.open("17-3.txt");
	int a,b,c,d,mmin=10000000,k=0;
	F>>a>>b>>c;
	for(;!F.eof();)
	{
		F>>d;
		if(a>b && b>c && c>d && a-d>1000)
		{
			++k;
			mmin=min(a+b+c+d,mmin);
		}
		a=b;
		b=c;
		c=d;
	}
	cout<<k<<" "<<mmin;
}
