def carbon_emission_factor_of_vehicle(fuel_used, emission_factor):
    return fuel_used*emission_factor

fuel_used = 1200
emission_factor = 2.3
print(carbon_emission_factor_of_vehicle(fuel_used, emission_factor))