// Автор: М. Нехорошева

#include <iostream>
using namespace std;

int main() 
{ 
	for (int A = 0; A <= 1000; A++)
	{
		bool k=true;
		for ( int x = 0; x <= 1000; x++) 

		 		if (!((x&51)==0 || (x&41)!=0|| (x&A)==0) )
				{
					k=false;
					break;		
				}	
				
		if(k)	
			cout << A << " ";
	}
}
