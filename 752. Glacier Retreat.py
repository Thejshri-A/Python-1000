def glacier_retreat(initial_area = 800, rate = 0.05, decades = 4):
    area=[initial_area]
    for i in range(decades):
        area.append(area[-1]*(1-rate))
    return area

print(glacier_retreat())