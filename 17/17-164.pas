##
assign(input, '17-3.txt');
var a:= ReadInteger; 
var b:= ReadInteger;
var kol := 0; 
var maxS := -10000*3;
while not Seekeof() do begin
  var c := ReadInteger;
  var P: BigInteger := BigInteger(a)*b*c; 
  var S := a + b + c;
  if (abs(S) mod 10 = 5) and (P mod 7=0) then begin
    inc( kol );
    if S > maxS then maxS := S;
  end;
  (a, b) := (b, c);
end;
print( kol, maxS );