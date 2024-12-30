def wind_energy_potential(area, speed, rho=1.225):
    return 0.5*rho*area*(speed**3)

area = 50
speed = 10
print(wind_energy_potential(area, speed))