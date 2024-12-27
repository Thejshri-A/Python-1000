def glacier_retreat(initial_distance, retreat_rate, years):
    retreat=[initial_distance]
    for i in range(years):
        retreat.append(retreat[-1]+retreat_rate)
    return retreat

initial_distance = 0
retreat_rate = 15
years = 4
print(glacier_retreat(initial_distance, retreat_rate, years))