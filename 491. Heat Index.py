def heat_index(temp, humidity):
    return temp + 0.5*(humidity-50)

temp = 30
humidity = 80
print(heat_index(temp,humidity))