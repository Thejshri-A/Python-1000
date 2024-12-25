def groundwater_decline(initial_level, withdrawal , years):
    level = [initial_level]
    for i in range(years):
        level.append(level[-1]-withdrawal)
    return level
initial_level = 500
withdrawal = 20
years = 5
print(groundwater_decline(initial_level, withdrawal, years))