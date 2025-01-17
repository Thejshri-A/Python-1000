def soil_erodability(erodibility = 0.3, rainfall = 50, slope = 10):
    return erodibility*rainfall*slope

print(soil_erodability())