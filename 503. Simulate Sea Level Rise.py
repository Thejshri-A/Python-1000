def simulate_sea_level_rise(initial_level, rate, years):
    level=[initial_level]
    for i in range(years):
        level.append(round(level[-1]+rate, 2))
    return level

initial_level = 5
rate = 0.3
years = 4
print(simulate_sea_level_rise(initial_level, rate, years))