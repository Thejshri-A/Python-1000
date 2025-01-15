def heat_index(temperature = 35, humidity = 70):
    return temperature+0.5*(humidity-50)

print(heat_index())