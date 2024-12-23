def soil_moisture_deficit(soil_capacity, current_moisture):
    return soil_capacity-current_moisture

soil_capacity = 100
current_moisture = 70
print(soil_moisture_deficit(soil_capacity, current_moisture))