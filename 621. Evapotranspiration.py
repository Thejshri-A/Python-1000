def evapotranspiration(constant, temperature, baseline):
    return constant*(temperature-baseline)

constant = 0.5
temperature = 30
baseline = 20
print(evapotranspiration(constant, temperature, baseline))