// Автор: М. Нехорошева

#include <iostream>

using namespace std ;

int main()
{
	string losos="";
	for(int i=0; i<2019; losos=losos+"1", i++);
	for(int i=0; i<2019; losos=losos+"2", i++);
	for(; losos.find("222")!=-1;){
		if(losos.find("222")!=-1)
			losos.replace(losos.find("222"),3,"1");
		if(losos.find("111")!=-1)
			losos.replace(losos.find("111"),3,"2");
	}
	cout<<losos;
}
