// Автор: М. Нехорошева

#include <iostream>
using namespace std;
int main ()
{
	int m=0;
	for (int a1=1;a1<101;++a1)
		for (int a2=1;a2<101;++a2)
		{
			bool f=true;
			for (int x=1;x<1000;++x)
			{
				bool P=(x>=44 && x<=49);
				bool Q=(x>=28 && x<=53);
				bool A=(x>=a1 && x<=a2);
				if (!((A<=P) || Q))
					{
						f=false;
						break;
					}
			}	
		if (f) 
			m=max(m,a2-a1);
		}
	cout<<m;
}

