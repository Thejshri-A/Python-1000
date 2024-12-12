def greenhouse_gas_emission(activity_level, emission_factor):
    return [round(level*emission_factor, 2) for level in activity_level]

activity_level = [100, 200]
emission_factor = 2.3
print("Greenhouse Gas Emission: ", greenhouse_gas_emission(activity_level, emission_factor))