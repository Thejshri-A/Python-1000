def renewable_energy_potential(capacity = 5, sunlight = [6, 5, 8], efficiency = 0.8):
    return [capacity*sunlit*efficiency for sunlit in sunlight]

print(renewable_energy_potential())