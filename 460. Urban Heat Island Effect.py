def urban_heat_island(urban_temps, rural_avg):
    islands=[]
    for i in range(len(urban_temps)):
        for j in range(len(urban_temps[0])):
            if urban_temps[i][j]>rural_avg+2:
                islands.append((i,j))
                
    return islands

urban_temps = [[30, 35], [32, 36]]
rural_avg = 32
print(urban_heat_island(urban_temps, rural_avg))