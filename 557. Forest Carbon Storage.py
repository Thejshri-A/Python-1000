def forest_carbon_storage(area, biomass_density, carbon_fraction):
    return area*biomass_density*carbon_fraction

area = 100
biomass_density = 10
carbon_fraction = 0.5
print("Carbon Storage : ", forest_carbon_storage(area, biomass_density, carbon_fraction), " tons")