def soil_erosion_risk(rainfall = 200, erodibility = 0.3, slope_factor = 1.5):
    return rainfall*erodibility*slope_factor

print(soil_erosion_risk())