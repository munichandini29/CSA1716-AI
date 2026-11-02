male(ram).
male(shyam).

female(sita).
female(gita).

parent(ram, shyam).
parent(sita, shyam).
parent(shyam, ravi).
parent(gita, ravi).

father(X,Y) :-
    parent(X,Y),
    male(X).

mother(X,Y) :-
    parent(X,Y),
    female(X).

grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).
?- father(ram,shyam).
?- grandparent(ram,ravi).
