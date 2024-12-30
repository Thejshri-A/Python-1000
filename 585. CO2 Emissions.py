def co2_emissions(distance, emission_factor):
    return distance*emission_factor

distance = 200
emission_factor = 0.2
print(co2_emissions(distance, emission_factor))