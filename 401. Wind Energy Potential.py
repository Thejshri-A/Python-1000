def wind_energy_potential(blade_area, winds):
    
    potential = []
    for wind in winds:
        poten = 0.5*1.2*blade_area*(wind**3)
        potential.append(poten)
    return potential
blade_area = 30
winds = [5, 10, 15]
print(wind_energy_potential(blade_area, winds))
    