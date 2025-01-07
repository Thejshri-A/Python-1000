def wind_energy_potential(wind_speeds = [4.5, 6.2, 7.8, 5.9]):
    threshold=6
    potential=[]
    for i,val in enumerate(wind_speeds):
        if val>6:
            potential.append(i+1)
    return potential

print(wind_energy_potential())