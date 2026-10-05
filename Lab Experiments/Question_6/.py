def vacuum_cleaner(room_a, room_b, position):
    rooms = {
        "A": room_a,
        "B": room_b
    }

    print("Initial State:")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Vacuum Position:", position)
    print()

    while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":

        if rooms[position] == "Dirty":
            print("Action: Suck")
            rooms[position] = "Clean"

        else:
            if position == "A":
                position = "B"
            else:
                position = "A"

            print("Action: Move to", position)

    print("\nFinal State:")
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Vacuum Position:", position)


# Initial condition
vacuum_cleaner("Dirty", "Dirty", "A")
