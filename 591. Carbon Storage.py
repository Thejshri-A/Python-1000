def carbon_storage(biomass, fraction):
    return sum([b*fraction for b in biomass])

biomass = [50, 100, 30]
fraction = 0.45
print(carbon_storage(biomass, fraction))