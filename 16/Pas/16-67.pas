program ss;
var n, k, s, x, d : integer;
function F(n, nest :integer): integer;                    
begin
   if nest > 100 then Result := -maxInt
   else if n < 3 then Result := n + 1
   else if (n mod 2 = 0) and (n >= 3) then Result := n+2*F(n+2, nest+1)
   else if (n mod 2 <> 0) and (n >= 3) then Result := F(n - 2, nest+1) + n-2
end;
begin
   k := 0;
   For n := 1  to 10000000 do begin
     x := F(n, 0);
     k += if (100 <= x) and (x < 1000) then 1 else 0;
   end;
   writeln(k);
end.