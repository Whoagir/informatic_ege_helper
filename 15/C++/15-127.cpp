// Автор: М. Нехорошева

#include <iostream>
using namespace std;

int main() 
{
	for (int A = 1; A <= 100; A++)
	{
		for (int x = 1; x <= 100; x++) 
		{
	  		bool F=(!(x & 25) != 0 ||!((x & 13) == 0) || (x&A)!=0);
			if (!F) break;
			if (x==100 )
				cout << A << " ";
		}
	}
}	
