def check(i,j):

    if i-1>=0 and abs(A[i-1][j] - A[i][j]) <= 10 and Mark[i-1][j] == 0:
        Mark[i-1][j] = 1
        check(i-1,j)

    if i+1<N and abs(A[i+1][j] - A[i][j]) <= 10 and Mark[i+1][j]==0:
        Mark[i+1][j] = 1
        check(i+1,j)
    if j+1 < N and abs(A[i][j+1]-A[i][j])<=10 and Mark[i][j+1]==0:
        Mark[i][j+1] = 1
        check(i, j+1)
    if j - 1 >= 0 and abs(A[i][j-1] - A[i][j]) <= 10 and Mark[i][j-1] == 0:
        Mark[i][j-1] = 1
        check(i, j-1)

A = [[10, 15, 40, 45],
     [12, 20, 42, 47],
     [30, 25, 35, 45],
     [80, 85, 92, 55]]
N = len(A)
Mark = [[0] * N for _ in range(N)]

Mark[0][0] = 1
check(0, 0)

for row in Mark:
    print(row)
