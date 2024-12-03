function F( n: integer ): integer; 
begin 
   if n < 4 then  
     Result := n-1 
   else if n mod 3 = 0  then  
     Result := n + 2*F(n-1) 
   else 
     Result := F(n-2) + F(n-3) 
end; 
begin 
   writeln( F(25).ToString.Select(x->StrToInt(x)).Sum ); 
end. 