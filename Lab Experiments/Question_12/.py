board = [[" "]*3 for _ in range(3)]

player = "X"

for move in range(9):
    for row in board:
        print(row)

    r = int(input("Row (0-2): "))
    c = int(input("Column (0-2): "))

    if board[r][c] == " ":
        board[r][c] = player
        player = "O" if player == "X" else "X"
    else:
        print("Already occupied!")

print("Final Board:")
for row in board:
    print(row)
