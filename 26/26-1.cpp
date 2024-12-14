// Автор: М. Нехорошева

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
int main() 
{
	fstream F;  //открываем файл в режиме чтения  
	F.open("26-1.txt");
	int S,N;
	F>>S>>N;
	int arr[N];
	int k=0,sum=0,m;
	for (int i=0;i<N;++i)
		F>>arr[i];
	sort   (arr,arr+N);
	for (;sum<=S;++k)
		sum+=arr[k];
	sum=sum-arr[k];
	--k;
	sum=sum-arr[k];	
	int r=S-sum;
	for (int i=N-1;i>=k;--i)
		if (sum+arr[i]<=S )
		{
			m=arr[i];
			break;
		}
		//else 
		//	if(r-arr[i]<0) break;
	cout<<k<<" "<<m;
				
}
