def evaporation_in_reservoir(water_level, evaporations):
    for evaporate in evaporations:
        water_level-=evaporate
    return water_level

water_level = 1000
evaporations = [10, 15, 20, 25]
print(evaporation_in_reservoir(water_level, evaporations))