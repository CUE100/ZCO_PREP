from collections import deque
start = (Ai , Bi)
grid = N * M
cost_list = [cost for _ in range(len(grid))]

moves = ((0, 1),(1,0 ))
def chef_land(grid,cost_list):

    dist = [cost_list] * grid
    dist[start] = cost_list[Ai][Bi]

    queue = deque()
    queue.append(start)
    minimum = cost_list[Ai][Bi]

    while queue:
        v,w = queue.popleft()

        for a,b in moves:
            new_x = v + a
            new_y = w + b

            if minimum > (dist[v][w] + dist[new_x][new_y]):
                minimum = dist[v][w] + dist[new_x][new_y]

    return minimum









