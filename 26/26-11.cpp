// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("26-11.txt");
	int n,S, g, max=-1;
	F>>S>>n;
	int a[n];
	for (int i=0;i<n;++i)
	{
		F>>a[i];
	}	
	sort(a,a+n,greater<int>());
	long int sum=0,i;
	for (i=0;sum<=S;++i)
	{
		if (sum+a[i]<S) sum+=a[i];
			else break;
	}
	cout << i << endl;
	g=(S-sum)+a[i-1];
	for (i=0;sum<=S;++i)
	{
		if (max<a[i] and a[i]<=g) max=a[i];
		if (a[i]>g) break;
	}
	cout << max;
	
}


