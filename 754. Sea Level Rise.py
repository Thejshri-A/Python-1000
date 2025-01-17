def sea_level_rise(initial_level = 0, melt_rate = 3.2, years = 5):
    level=[initial_level]
    for i in range(years):
        level.append(level[-1]+melt_rate)
    return level

print(sea_level_rise())