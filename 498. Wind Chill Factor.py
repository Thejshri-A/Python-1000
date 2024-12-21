def wind_chill_factor(temp, velocity):
    return temp-0.7*velocity

temp = 10
velocity = 20
print("Wind Chill : ", wind_chill_factor(temp, velocity))