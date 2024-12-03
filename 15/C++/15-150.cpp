// Автор: М. Нехорошева

#include <iostream>
using namespace std;

int main() 
{
for (int A = 1; A <= 10000; A++)
{
	for (int x = 1; x <= 10000; x++) 
	{
		if (!((!((x & A) != 0 )|| !((x & 36) == 0) || ((x & 6) != 0 ))))
			{
				break;
			}
		if (x == 10000)
			cout << A << " ";
	}	
	
}

}	
