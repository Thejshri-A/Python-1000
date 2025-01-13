def snowmelt_runoff(snowpack = 100, temp_increase = 5, melt_rate = 0.1):
    return snowpack*(temp_increase*melt_rate)

print(snowmelt_runoff())