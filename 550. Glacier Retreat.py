def glacier_retreat(initial_distance, rate, years):
    retreat=[initial_distance]
    for i in range(years):
        retreat.append(retreat[-1]+rate)
    return retreat

initial_distance = 0
rate = 5
years = 4
print(glacier_retreat(initial_distance, rate, years))