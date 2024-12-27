def evapotranspiration_level(initial_level, evapotranspiration):
    level=[initial_level]
    for i in range(len(evapotranspiration)):
        level.append(level[-1]-evapotranspiration[i])
    return level

initial_level = 100
evapotranspiration = [5, 7, 10]
print(evapotranspiration_level(initial_level, evapotranspiration))