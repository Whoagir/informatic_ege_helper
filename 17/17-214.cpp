// Автор: М. Нехорошева

# include <iostream>
# include <fstream>
using namespace std;
int main ()
{
	fstream f;
	f.open("17-4.txt");
	int n1=10000000,n;
	int a[n1];
	int x;
	f>>x;
	cout<<x;
//	float s=0;
//	for (n=0;f>>x;a[n]=x,s+=x,++n);
//	s=(float)s/n;
//	cout<<n;
//	int k=0,ms=1000000;
//	for (int i=0;i<n-1;++i)
//		if (a[i]<s && a[i+1]<s && (a[i]+a[i+1])%100==19)
//			{
//				++k;
//				ms=min(ms,(a[i]+a[i+1]));
//			}
//	cout<<k<<" "<<ms;
}
