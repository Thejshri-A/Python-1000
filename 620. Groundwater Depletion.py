def groundwater_depletion(initial_level, withdrawal, years):
    level=[initial_level]
    for i in range(years):
        level.append(level[-1] - withdrawal)
    return level

initial_level = 100
withdrawal = 5
years = 4
print(groundwater_depletion(initial_level, withdrawal, years))