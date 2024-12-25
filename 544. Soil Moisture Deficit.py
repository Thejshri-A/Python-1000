def soil_moisture_deficit(field_capacity, current_moisture):
    return field_capacity-current_moisture

field_capacity = 30
current_moisture = 20
print(soil_moisture_deficit(field_capacity, current_moisture))