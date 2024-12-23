def heat_index(temp, humidity):
    return temp+0.5*humidity

temp = 30
humidity = 60
print(heat_index(temp, humidity))