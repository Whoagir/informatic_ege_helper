// Автор: Зубов Н.С.
function G (n:integer):integer;forward;
function F (n:integer):integer;
begin
if n=1 then 
  F:=1
else 
  F:=3*F(n-1)+G(n-1)-n+5
end;
function G(n:integer):integer;
begin
if n=1 then 
  G:=1
else 
  G:=F(n-1)+3*G(n-1)-3*n
end;
begin
write(F(14)+G(14));
end.
