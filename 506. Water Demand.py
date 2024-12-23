def water_demand(population, per_capita_use):
    return population*per_capita_use

population = 100000
per_capita_use = 150
print(water_demand(population, per_capita_use)," L/day")