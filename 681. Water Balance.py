def water_balance(precipitation = 120, evapotranspiration = 50, runoff = 30):
    return precipitation-(evapotranspiration+runoff)

print(water_balance())