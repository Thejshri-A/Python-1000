def forest_expansion(initial_area, rate, years):
    area=[initial_area]
    for i in range(years):
        area.append(area[-1]*(1+rate))
    return area

initial_area = 1000
rate = 0.02
years = 3
print(forest_expansion(initial_area, rate, years))