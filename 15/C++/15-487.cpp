// Автор: М. Нехорошева

#include <iostream>
using namespace std;
int main ()
{
	int m=10000;
	for (int a1=1;a1<1010;++a1)
		for (int a2=1;a2<1010;++a2)
		{
			bool f=true;
			for (int x=1;x<1000;++x)
			{
				bool P=(x>=50 && x<=200);
				bool R=(x>=350 && x<=500);
				bool Q=(x>=150 && x<=250);
				bool A=(x>=a1 && x<=a2);
				if (!((P<=Q) || (!A<=!R)))
					{
						f=false;
						break;
					}
			}	
		if (f) 
			m=min(m,a2-a1);
		}
	cout<<m;
}
