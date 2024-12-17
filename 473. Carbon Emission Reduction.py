def carbon_emission_reduction(initial,rate, years):
    emission=[initial]
    
    for i in range(years):
        emission.append(emission[-1]*(1-rate))
    
    return emission

initial = 1000
rate = 0.05
years = 3
print(carbon_emission_reduction(initial,rate, years))