def soil_erosion_simulation(rainfall_intensity, soil_erodibility, soil_area):
    return [rainfall_intensity*soil_erodibility*area for area in soil_area]

rainfall_intensity = 50
soil_erodibility = 0.3
soil_area = [100, 200]
print("Soil Erosion Simulation : ", soil_erosion_simulation(rainfall_intensity, soil_erodibility, soil_area))