// Автор: М. Нехорошева

#include<iostream>
#include<string>
using namespace std;
int main(){
	string s(107,'8');
	
	for(;s.find("555")!=-1 || s.find("888")!=-1;){
		if(s.find("555")!=-1)
			s.replace(s.find("555"),3,"8");
		if(s.find("888")!=-1)
			s.replace(s.find("888"),3,"5");
	}
	cout<<s;
}
