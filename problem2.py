def find_saddle_point_coordinates(grid):
    column_coordinate = 0
    row_coordinate = 0
    column_list = []
    n = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == min(grid[i]):
                for k in range(len(grid)):
                    column_list.append(grid[k][j])
                if grid[i][j] == max(column_list):
                    row_coordinate = i
                    column_coordinate = j
                    n = 1
    if n:
        return (row_coordinate, column_coordinate)
    else:
        return None

grid = [[5, 6, 7], 
 [4, 2, 1], 
 [3, 0,-1]]

print(find_saddle_point_coordinates(grid))

