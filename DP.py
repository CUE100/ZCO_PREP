def dynamic_programming(rows=3,cols=3):

    ways = [[0] * cols for _ in range(rows)]
    ways[1][0] = 0

    for i in range(rows):
        for j in range(cols):
            if i == 1 and j ==0:
                continue
            elif i == 0 or j == 0:
                ways[i][j] = 1
            else:
                ways[i][j] = ways[i-1][j] + ways[i][j-1]
    print(ways[rows-1][cols-1])

dynamic_programming(rows=3,cols=3)