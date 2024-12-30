def wind_energy_potential(density, area, speed, time):
    return 0.5*density*area*time*(speed**3)

density = 1.2
area = 50
speed = 10
time = 5
print(wind_energy_potential(density, area, speed, time))