move_to_box :-
    write('Monkey moves to the box'), nl.

push_box :-
    write('Monkey pushes the box under the banana'), nl.

climb_box :-
    write('Monkey climbs the box'), nl.

grab_banana :-
    write('Monkey grabs the banana'), nl.

solve :-
    move_to_box,
    push_box,
    climb_box,
    grab_banana.
?- solve.
