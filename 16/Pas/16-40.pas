// Автор: Зубов Н.С.
function G (n:integer):integer;forward;
function F (n:integer):integer;
begin
if n=1 then 
  F:=1
else 
  F:=F(n-1)-n*G(n-1)
end;
function G(n:integer):integer;
begin
if n=1 then 
  G:=1
else 
  G:=F(n-1)+2*G(n-1)
end;
begin
write(G(18));
end.
