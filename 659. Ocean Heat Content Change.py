def ocean_heat_content_change(specific_heat, mass, temperature_change):
    return specific_heat*mass*temperature_change

specific_heat = 4186
mass = 1000
temperature_change = 2
print(ocean_heat_content_change(specific_heat, mass, temperature_change))