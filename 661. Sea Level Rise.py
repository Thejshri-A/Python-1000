def sea_level_rise(initial_rise, rate, years):
    rise=[initial_rise]
    for i in range(years):
        rise.append(rise[-1]+rate)
    return rise

initial_rise = 10
rate = 3
years = 5
print(sea_level_rise(initial_rise, rate, years))