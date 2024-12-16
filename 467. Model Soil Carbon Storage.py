def model_soil_carbon_storage(bulk_density, depth, carbon_fraction):
    return bulk_density*depth*carbon_fraction


bulk_density = 1.2
depth = 30
carbon_fraction = 0.02
print(model_soil_carbon_storage(bulk_density, depth, carbon_fraction), "g/cm2")