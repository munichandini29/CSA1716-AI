graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if neighbor in result and result[neighbor] == color:
            return False
    return True

def solve(node_list):
    if not node_list:
        return True

    node = node_list[0]

    for color in colors:
        if is_safe(node, color):
            result[node] = color
            if solve(node_list[1:]):
                return True
            result.pop(node)

    return False

solve(list(graph.keys()))

print("Color Assignment:")
for node in result:
    print(node, "->", result[node])
