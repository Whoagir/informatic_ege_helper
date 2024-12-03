// Автор: М. Нехорошева

#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main(){
	string s(string(1,'1')+string(33,'0'));
	
	for(;s.find("1")!=-1 || s.find("100")!=-1;){
		if(s.find("100")!=-1)
			s.replace(s.find("100"),3,"0001");
		else
			s.replace(s.find("1"),1,"00");
	}
//	cout<<s<<endl;
	cout<<count(s.begin(),s.end(),'0');
}
