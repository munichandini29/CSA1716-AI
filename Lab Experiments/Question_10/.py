graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

open_list = ['A']
closed_list = []

g = {'A': 0}
parent = {'A': 'A'}

goal = 'F'

while open_list:
    n = min(open_list, key=lambda x: g[x] + heuristic[x])

    if n == goal:
        path = []

        while parent[n] != n:
            path.append(n)
            n = parent[n]

        path.append('A')
        path.reverse()

        print("Path:", path)
        print("Cost:", g[goal])
        break

    open_list.remove(n)
    closed_list.append(n)

    for m, weight in graph[n].items():
        if m not in open_list and m not in closed_list:
            open_list.append(m)
            parent[m] = n
            g[m] = g[n] + weight
