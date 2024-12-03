// Автор: М. Нехорошева

//Алгоритм вычисления функции F(n), где n - натуральное число, задан следующими соотношениями:
//F(n) = 1,  при n < 2,
//F(n) = F(n / 3) + 1, когда n >=2 и делится на 3,
//F(n) = F(n - 2) + 5 , когда n >= 2 и не делится на 3.
//Назовите количество значений n на отрезке [1;100000], для которых F(n) равно 55.
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
using namespace std;
int F(int n)
{
	if(n<2) 
		return 1;
	else
		if(n%3==0)
			return F(n/3)+1;
			else return F(n-2)+5;
}
 int main()
 {
 	int k=0;
 	for (int i=1;i<=100000;++i)
 		if( F(i)==55)
 			++k;
 	cout<<k;
 }

