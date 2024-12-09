def daily_solar_production(radiations):
    efficiency =  0.15 #Given
    total_prod= sum(radiations)*efficiency
    return total_prod

radiations = [0.5, 1.0, 1.2, 0.8]
print(daily_solar_production(radiations))