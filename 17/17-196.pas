##
var data := ReadLines('17-10.txt').Select(t -> t.ToInteger).ToArray;
var triples := data.NWise(3).Select(ar->ar.Order.ToArray)
    .Where(ar->ar[0]*ar[0]+ar[1]*ar[1]=ar[2]*ar[2]);
triples.Count.Print;    
triples.Sum(t->t[2]).Print;    
