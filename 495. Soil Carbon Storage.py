def soil_carbon_storage(area, density, thickness):
    return area*density*thickness
area = 100
density = 0.5
thickness = 2
print(soil_carbon_storage(area, density, thickness))