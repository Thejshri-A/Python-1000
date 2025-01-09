def permafrost_thaw(initial_area = 2000, rate = 0.02, years = 3):
    area=[initial_area]
    
    for i in range(years):
        area.append(area[-1]*(1+rate))
    return area

print(permafrost_thaw())