def forest_regrowth_after_fire(initial_area, rate, years):
    area=[initial_area]
    for i in range(years):
        area.append(area[-1]*(1+rate))
    return area

initial_area = 50
rate = 0.1
years = 3
print(forest_regrowth_after_fire(initial_area, rate, years))