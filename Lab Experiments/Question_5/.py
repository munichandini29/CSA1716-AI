from collections import deque

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    # Values must be within limits
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    # Left side condition
    if m_left > 0 and m_left < c_left:
        return False

    # Right side condition
    if m_right > 0 and m_right < c_right:
        return False

    return True


def solve():
    start = (3, 3, 0)  # 0 = Left, 1 = Right
    goal = (0, 0, 1)

    # Possible boat combinations
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    queue = deque()
    queue.append((start, [start]))

    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        m, c, boat = state

        for dm, dc in moves:

            if boat == 0:  # Boat on left
                new_m = m - dm
                new_c = c - dc
                new_boat = 1
            else:  # Boat on right
                new_m = m + dm
                new_c = c + dc
                new_boat = 0

            new_state = (new_m, new_c, new_boat)

            if is_valid(new_m, new_c) and new_state not in visited:
                visited.add(new_state)
                queue.append(
                    (new_state, path + [new_state])
                )

    return None


solution = solve()

if solution:
    print("Missionaries and Cannibals Solution:\n")

    for i, state in enumerate(solution):
        m, c, boat = state

        side = "Left" if boat == 0 else "Right"

        print(
            f"Step {i}: "
            f"Missionaries Left = {m}, "
            f"Cannibals Left = {c}, "
            f"Boat = {side}"
        )
else:
    print("No solution exists.")
