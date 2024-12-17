def river_flood_level(levels, threshold):
    return [i+1 for i,val in enumerate(levels) if val>threshold ]

levels = [5, 7, 12, 8]
threshold = 10
print(river_flood_level(levels, threshold))