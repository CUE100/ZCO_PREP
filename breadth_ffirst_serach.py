from collections import deque

A = [[10, 15, 40, 45],
     [12, 20, 42, 47],
     [30, 25, 35, 45],
     [80, 85, 92, 55]]

N = len(A)

Mark = [[0] * N for _ in range(N)]
Dist = [[0] * N for _ in range(N)]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

Mark[0][0] = 1
Dist[0][0] = 0

queue = deque()
queue.append((0, 0))

while queue:
        row, col = queue.popleft()
        for move_row, move_col in moves:

            new_row = row + move_row
            new_col = col + move_col

            if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
                continue

            if Mark[new_row][new_col] == 1:
                continue

            if abs(A[new_row][new_col] - A[row][col]) > 10:
                continue

            Mark[new_row][new_col] = 1
            Dist[new_row][new_col] = Dist[row][col] + 1
            queue.append((new_row, new_col))
            