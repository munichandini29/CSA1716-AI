import math

scores = [3, 5, 6, 9]

def alphabeta(depth, node, maximizing, alpha, beta):
    if depth == 2:
        return scores[node]

    if maximizing:
        value = -math.inf
        for i in range(2):
            value = max(value,
                        alphabeta(depth+1, node*2+i, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = math.inf
        for i in range(2):
            value = min(value,
                        alphabeta(depth+1, node*2+i, True, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

print("Optimal Value:",
      alphabeta(0, 0, True, -math.inf, math.inf))
