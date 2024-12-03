#include<iostream> 
 using namespace std; 
 int main() 
 { 
    string s(170, '7');  

    int p777= s.find("777"); 
    
    while( p777 != string::npos  ) { 
        int p77 = s.find("77"); 
		s.replace( p77, 2, "2" ); 
        int p22 = s.find("22"); 
        if( p22 != string::npos ) 
          s.replace( p22, 2, "7" );   
        p777= s.find("777"); 
        } 
    cout << s; 
 }
