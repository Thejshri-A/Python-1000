def high_air_pollution(air_data, threshold):
    
    return sum(1 for air in air_data if air>=threshold)

air_data = [150, 200, 300, 50, 100]
threshold = 200
print(high_air_pollution(air_data, threshold))