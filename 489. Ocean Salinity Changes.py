def ocean_salinity_changes(initial_salinity, inflow, evaporation):
    curr_salinity = [initial_salinity]
    for i,e in zip(inflow, evaporation):
        curr_salinity.append(curr_salinity[-1]-i+e)
    
    return curr_salinity[1:]

initial_salinity = 35
inflow = [1,2]
evaporation = [3,1] 
print(ocean_salinity_changes(initial_salinity, inflow, evaporation))