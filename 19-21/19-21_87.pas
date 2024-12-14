###
function h(s:int) := |s+3,s+13,s+23|;

function win(s:int) := s>=73;

var g := (1..72).ToHS;
var W1 := g.Wh(x->h(x).Any(x->win(x))).ToHS; g-=W1;
var L1 := g.Wh(x->h(x).All(x->x in W1)).ToHS; g-=L1;
var W2 := g.Wh(x->h(x).Any(x->x in L1)).ToHS;
println(W1,L1,W2);

var z := (1..23);
// Найдите минимальное начальное s, когда 
// Петя сходил неудачно и Ваня выиграл первым ходом
prln('19)',z.Wh(s->h(2+3*s).Any(x->x in W1)).Min); 

// Петя выигрывает на втором ходу при любом ходе Вани
prln('20)',z.Wh(s->h(2+3*s).Any(x->x in L1)));

// Петя не может выиграть, но может проиграть как на первом,так и на втором ходу
prln('21)',z.Wh(s->h(2+3*s).All(x-> x in (W1+W2))
               and h(2+3*s).Any(x->x in W2)
               and h(2+3*s).Any(x->x in W1)));


