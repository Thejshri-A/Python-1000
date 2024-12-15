def emission(emission_factor, activity_data):
    return [round(emission_factor*data) for data in activity_data]

emission_factor = 2.3
activity_data = [100, 200, 300]
print(emission(emission_factor, activity_data))