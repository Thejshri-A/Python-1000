def solar_energy_prediction(irradiance, area, efficiency):
    return irradiance*area*efficiency
irradiance = 1000
area = 10
efficiency = 0.15
print(solar_energy_prediction(irradiance, area, efficiency))