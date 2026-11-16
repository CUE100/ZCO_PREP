matrix = [[0] * (n + 1) for _ in range(n + 1)]   # (n+1) x (n+1) grid of zeros
for a, b in edges:                               # go through each pair
    matrix[a][b] = 1                             # a is a neighbour of b
    matrix[b][a] = 1                             # and b is a neighbour of a