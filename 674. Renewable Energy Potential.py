def renewable_energy_potential(radiation = 1000, efficiency = 0.15, area = 10):
    return radiation*efficiency*area

print(renewable_energy_potential())