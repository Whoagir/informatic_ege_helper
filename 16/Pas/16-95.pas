// Автор: Зубов Н.С.
function G (n:BigInteger):BigInteger;forward;
function F (n:BigInteger):BigInteger;
begin
if n<10 then 
  F:=n;
if n>=10 then 
  F:=F(G(n));
end;
function G(n:BigInteger):BigInteger;
begin
if n<10 then 
  G:=n
else 
  G:=n mod 10 + G(n div 10);
end;
begin     
write(F(12345678987654321));
end.