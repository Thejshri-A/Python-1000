def compute_solar_power(radiation, efficiency, area):
    total= sum(radiation)*efficiency*area
    return total
radiation = [5, 6, 7, 4]
efficiency = 0.2
area = 2
print(compute_solar_power(radiation, efficiency, area))