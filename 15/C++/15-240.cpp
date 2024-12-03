// Автор: М. Нехорошева

#include <iostream>
using namespace std;

int main() 
{ 
	for (int A = 1; A <= 1000; A++)
	{
		bool k=true;
		for ( int x = 0; x <= 1000; x++) 
	 		for ( int y = 0; y <= 1000; y++) 
		 		if (!((2*x+3*y<30 || x+y>=A)))
				{
					k=false;
					break;	
				}
		if(k)	
			cout << A << " ";
	}
}
