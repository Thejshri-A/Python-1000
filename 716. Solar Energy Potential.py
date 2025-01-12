def solar_energy_potential(irradiance = 6, area = 20, efficiency = 0.15):
    return irradiance*area*efficiency

print(solar_energy_potential(), "kWh")