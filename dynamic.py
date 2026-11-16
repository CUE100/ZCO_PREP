def dynamic_programming(grid):
    cols = len(grid[0])
    rows = len(grid)

    total = 0
    total_minimum  = grid[0][0]
    for i in range(rows-1):
        for j in range(cols-1):
            total_minimum = min(grid[i+1][j] , grid[i][j+1])
            total += total_minimum
    print(total)

grid = [[  1,  3 , 1],
  [1,  5 , 1],
  [4 , 2 , 1]]

dynamic_programming(grid) #