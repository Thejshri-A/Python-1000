def carbon_sequestration_potential(rate_per_hectare, area):
    return rate_per_hectare*area
rate_per_hectare = 10
area = 200
print(carbon_sequestration_potential(rate_per_hectare, area))