from collections import deque

dist = [-1] * (n+1)
dist[start] = 0

queue = deque()
queue.append(start)

while queue:
    v = queue.popleft()
    for w in neighbours[v]:
        if dist[w]==-1:
            dist[w] = dist[v] + 1
            queue.append(w)