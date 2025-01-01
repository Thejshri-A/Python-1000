def ocean_wave_energy(density, gravity, height):
    return 0.5*density*gravity*(height**2)

density = 1025
gravity = 9.8
height = 2.5
print(ocean_wave_energy(density, gravity, height))