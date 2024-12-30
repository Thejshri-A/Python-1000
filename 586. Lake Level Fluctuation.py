def lake_level_fluctuations(initial_level, inflows, outflows):
    level=[initial_level]
    for i,o in zip(inflows, outflows):
        level.append(level[-1]+i-o)
    return level

initial_level = 500
inflows = [50, 40]
outflows = [30, 20]
print(lake_level_fluctuations(initial_level, inflows, outflows))