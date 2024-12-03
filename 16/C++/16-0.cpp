// Автор: М. Нехорошева

#include <iostream>
using namespace std;

int sumDigits ( int n )
{int sum; 
for (sum = 0;n; n /= 10) 
    sum += n % 10;
  return sum;
}

 int main()
 {

 	cout<<sumDigits(12345);
 }

