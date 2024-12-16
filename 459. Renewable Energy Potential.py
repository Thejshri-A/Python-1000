def renewable_energy_potential(blade_area, wind_speed, time, density=1.225):
    return 0.5*density*blade_area*wind_speed*time

blade_area = 10
wind_speed = 12
time = 5
print("Renewable Energy Potential : ", renewable_energy_potential(blade_area, wind_speed, time))