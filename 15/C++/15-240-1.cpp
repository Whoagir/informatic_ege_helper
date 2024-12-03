// Автор: М. Нехорошева

#include <iostream>
using namespace std;
bool f( int x, int y, int A )
  {
  	return (x>9 || x*x <= A) && (y*y > A) || (y <= 10);
  }

int main() 
{ int x,y;
	for (int A = 1; A <= 1000; A++)
	{
		bool k=true;
		for ( x = 1; x <= 1000; x++) 
	 		for ( y = 1; y <= 1000; y++) 
		 		if (!((x>9 || x*x <= A) && (y*y > A) || (y <= 10)))
				{
					k=false;
					break;	
				}
		if(k)	
			cout << A << " ";
	}

}
