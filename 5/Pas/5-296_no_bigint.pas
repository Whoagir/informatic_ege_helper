var sEven, sOdd: integer;

function modDigit( n: integer ): integer;
begin
  n := 2*n;
  Result := n div 10 + n mod 10;  
end;

function is_correct( n: integer ): boolean;
begin
  var s := sEven + sOdd;
  var isEven := True;
  while n > 0 do begin
    s += isEven ? n mod 10 : modDigit(n mod 10);
    n := n div 10;
    isEven := not isEven;
  end;  
  Result := s mod 10 = 0
end;

begin
  sEven := 8 + 6 + 4 + 2;
  sOdd := modDigit(7) + modDigit(5) + modDigit(3) + modDigit(1);
  var num := 91011121 + 1;
  while not is_correct(num) do num += 1;
  print( num )
end.