def cyclone_risk_zones(grid):
    cyclone=[]
    for i, row in enumerate(grid):
        for j, wind_speed in enumerate(row):
            if wind_speed>100:
                cyclone.append((i,j))
    return cyclone
grid=[[80, 110], [90, 120]]
print(cyclone_risk_zones(grid))