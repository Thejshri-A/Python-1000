def glacier_retreat(initial_area = 100, rate = 0.02, years = 5):
    area=[initial_area]
    for i in range(years):
        area.append(area[-1]*(1-rate))
    return area

print(glacier_retreat())