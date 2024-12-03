// Автор: Зубов Н.С.
function G (n:integer):integer;forward;
function F (n:integer):integer;
begin
if n=1 then 
  F:=1
else 
  F:=2*F(n-1)+G(n-1)-2*n
end;
function G(n:integer):integer;
begin
if n=1 then 
  G:=1
else 
  G:=F(n-1)+2*G(n-1)+n
end;
begin
write(F(14)+G(14));
end.
