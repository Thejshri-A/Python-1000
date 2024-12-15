def identify_deforestation_hotspots(grid):
    hotspots=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]<=20:
                hotspots.append((i,j))
    return hotspots

grid = [[50, 15], [30, 10]]
print(identify_deforestation_hotspots(grid))