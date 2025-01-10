def wind_energy_potential(density = 1.225, area = 50, speed = 10):
    return 0.5*density*area*(speed**3)

print(wind_energy_potential())