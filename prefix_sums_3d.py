P = [[0] * (cols + 1) for _ in range(rows + 1)]
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        P[i][j] = A[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
# total of the rectangle top..bottom, left..right:
P[bottom][right] - P[top-1][right] - P[bottom][left-1] + P[top-1][left-1]