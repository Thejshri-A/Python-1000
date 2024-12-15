def simulate_ocean_currents(grid):
    direction_map={"N":"North", "E": "East", "S": "South", "W":"West"}
    path=[]
    
    for row in grid:
        for speed, direction in row:
            if speed>0:
                path.append(direction_map[direction])
    return "->".join(path)

grid = [[(1, 'N'), (2, 'E')], [(3, 'S'), (0, 'W')]]
print("Object Moves: ", simulate_ocean_currents(grid))