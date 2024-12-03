// Автор: М. Нехорошева

#include <iostream>
#include <ctime>
#include <cstdlib>
#include <algorithm>
using namespace std;
int irand ( int a, int b )
{  return a + rand()% (b - a + 1);}
int main()
{
   int count;
   cin >> count;
   int arr[count];
   srand(time(NULL));	
   for (int i = 0; i < count; i++)
        {
	arr[i] = irand(-1000,1000);
	cout << arr[i] << " ";
        }
    cout << endl; 
    cout << endl;
    int k=0,s_min=1e9;
    for (int i = 0; i < count-1; i++)
    	if(arr[i]%7==0 && arr[i+1]%17 || arr[i+1]%7==0 && arr[i]%17)
    		k++, s_min=min(s_min,arr[i]+arr[i+1]), cout<<arr[i]<<"  "<<arr[i+1];
	cout<<endl<<k<<" "<<s_min;	
}

