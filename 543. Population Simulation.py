def population_simulation(initial_population, rate, capacity, years):
    population=[initial_population]
    for i in range(years):
        population.append(population[-1] + rate*population[-1]*(1-(population[-1]/capacity)))
    return population
    
initial_population = 50
rate = 0.1
capacity = 100
years = 3
print(population_simulation(initial_population, rate, capacity, years))