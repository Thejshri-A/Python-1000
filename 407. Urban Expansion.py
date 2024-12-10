def urban_expansion(population, rate):
    
    return round(population[-1]*(1+rate))

population = [1000, 1100, 1210] 
rate = 0.1

print(urban_expansion(population, rate))
    