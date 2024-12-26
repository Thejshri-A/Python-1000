def model_sea_level_rise(initial_level, rate, years):
    levels=[initial_level]
    for i in range(years):
        levels.append(levels[-1]+rate)
    return levels

initial_level = 0
rate = 3.3
years = 5
print(model_sea_level_rise(initial_level, rate, years))