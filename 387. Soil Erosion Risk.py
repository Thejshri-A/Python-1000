def soil_erosion_risk(rainfall, slope):
    return [r*s for r,s in zip(rainfall,slope)]

rainfall = [100, 200]
slope = [0.2, 0.3]
print(soil_erosion_risk(rainfall, slope))