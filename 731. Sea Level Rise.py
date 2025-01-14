def sea_level_rise(initial_level = 0, contributions = [2.5, 3.0, 2.8]):
    level=[contributions[0]]
    for i in range(1, len(contributions)):
        level.append(level[-1]+contributions[i])
    return level

print(sea_level_rise())