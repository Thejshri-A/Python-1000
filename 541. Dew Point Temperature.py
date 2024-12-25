def dew_point_temperature(temperature, humidity):
    return temperature-((100-humidity)/5)

temperature = 30
humidity = 60

print(dew_point_temperature(temperature, humidity))