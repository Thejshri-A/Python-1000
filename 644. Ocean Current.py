def ocean_current(speeds = [1.5, 2.0, 1.8, 1.2]):
    return sum(speeds)/len(speeds)

print(ocean_current())