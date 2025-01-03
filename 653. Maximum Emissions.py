def maximum_emissions(emissions):
    
    
    return max(emissions, key=emissions.get)

emissions = {'Asia': 20, 'Europe': 15, 'Africa': 5}
print(maximum_emissions(emissions))