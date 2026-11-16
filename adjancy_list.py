neighbours=[[] for _ in range(n+1)]

for a,b in edges:
    neighbours[a].append(b)
    neighbours[b].append(a)