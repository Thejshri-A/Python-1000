def urban_heat_island(t_urban, t_rural):
    urban_heat_island=[]
    for t_u, t_r in zip(t_urban, t_rural):
        urban_heat_island.append(t_u-t_r)
    return urban_heat_island

t_urban = [35, 36]
t_rural = [32, 33]
print(urban_heat_island(t_urban, t_rural))
        