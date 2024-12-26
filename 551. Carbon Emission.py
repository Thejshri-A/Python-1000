def carbon_emission(carbon_emission_factor, fuel_consumed):
    return carbon_emission_factor*fuel_consumed

carbon_emission_factor = 2.31
fuel_consumed = 100
print("Carbon Emission : ", carbon_emission(carbon_emission_factor, fuel_consumed))