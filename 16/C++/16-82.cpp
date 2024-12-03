// Автор: М. Нехорошева

//Алгоритм вычисления функции F(n), где n - натуральное число, задан следующими соотношениями:
//F(n) = n, при n <= 5,
//F(n) = n + F(n / 2 - 1), когда n > 5 и делится на 4,
//F(n) = n + F(n + 2) , когда n > 5 и не делится на 4.
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
using namespace std;
int F(int n)
{
	if(n<=1) 
		return n;
	else
		if(n%3==0)
			return n+F(n/3-1);
			else return 0;
}
 int main()
 {
 	int k=0,ma=0;
  	for (int i=1000;;++i)
 		{
 			if (F(i)>1000)
 			{
 				cout <<i<<"   "<<F(i);
 				break;
 			}
 		}
 	
 }

