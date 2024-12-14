###
assign(input,'26-57.txt');
var (n,m) := ri2;
var a := rai(n).OrdD.ToList;
println(a);
var l := 0; var k := 0; var i:=0;
while i<a.Count do begin
  if l+a[i]<=m then begin
    l += a[i]; 
    print(a[i]);
    i += 1;
  end;
  if (l=m) or (l<m)and(i<a.Count)and(l+a[i]>m) then begin
    if i=0 then break;
    a.RemoveRange(0,i);
    var d := m-l;
    k += i-1;
    if d>0 then begin
      var y := a.Wh(x->x>=d).Last;
      a.Remove(y);
      print(y);
      if y-d>0 then a.Add(y-d); 
      SortDescending(a);
      print('обрезь',y-d);    
      k += 1;
    end;
    i := 0; l := 0;
    println;//(a, k)
  end 
end;
println;
print(k, a.Count );

(*
10 30  17 15 14 12 11 8 6 4 3 2
