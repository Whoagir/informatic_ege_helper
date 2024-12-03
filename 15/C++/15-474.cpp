// Автор: М. Нехорошева

#include <iostream>
using namespace std;
int main ()
{
	int m=0;
	for (int a1=1;a1<1010;++a1)
		for (int a2=1;a2<1010;++a2)
		{
			bool f=true;
			for (int x=1;x<1010;++x)
			{
				bool P=(x>=150 && x<=400);
				bool Q=(x>=350 && x<=600);
				bool A=(x>=a1 && x<=a2);
				if (((!Q || P) && A))
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

