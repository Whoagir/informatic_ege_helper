// Автор: М. Нехорошева

#include<iostream>
#include<string>
using namespace std;
int main(){
	int n=6;
	string s=(string(15,'3')+string(18,'2')+string(n,'1'));
//	cout<<s<<endl;
	for(;s.find("31")!=-1  || s.find("33")!=-1 || s.find("21")!=-1;){
		if(s.find("31")!=-1)
			s.replace(s.find("31"),2,"123");
		if(s.find("33")!=-1)
			s.replace(s.find("33"),2,"211");
		if(s.find("21")!=-1)
			s.replace(s.find("21"),2,"1");
	}
	int sum=0;
	for(int i=0;i<s.size();i++)
		sum+=s[i]-'0';
	if(sum>24)
		cout<<n;
	else cout<<"NO";
}
