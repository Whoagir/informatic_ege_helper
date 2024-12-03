// Автор: М. Нехорошева

#include<iostream>
using namespace std;
int main(){
	for(int n = 0; n < 10000; ++n) {
		string s = string(1,'7') + string(n + 1,'1') + string(n + 2,'2') + string(n + 3,'3');
		for(; s.find("71") != -1 || s.find("72") != -1 || s.find("73") != -1 ;){
			if( s.find("71") != -1 )
				s.replace(s.find("71"),2,"227");
			if( s.find("72") != -1 )
				s.replace(s.find("72"),2,"37");
			if( s.find("73") != -1 )
				s.replace(s.find("73"),2,"17");		
		}
		int sum = 0;
		sum = (n+2)*3 + (n+1)*4 + (n+3) + 7;
		if(sum == 9 * n) {
			cout<<n<<endl;
			break;
		}
	}
	
}
