def algae_bloom_growth(initial_biomass = 100, rate = 0.2, days = 4):
    biomass=[initial_biomass]
    for i in range(days):
        biomass.append(biomass[-1]*(1+rate))
    return biomass

print(algae_bloom_growth())