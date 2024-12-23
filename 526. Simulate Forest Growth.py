def forest_growth(initial_area, rate, decades):
    growth=[initial_area]
    for i in range(decades):
        growth.append(growth[-1]*(1+rate))
    return growth

initial_area = 1000
rate = 0.02
decades = 3
print(forest_growth(initial_area, rate, decades))