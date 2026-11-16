def build_2d(A):
    rows = len(A)
    cols = len(A[0])
    P = [[0] * (cols + 1) for _ in range(rows + 1)]     # extra row and column of 0s
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            P[i][j] = A[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
    return P
