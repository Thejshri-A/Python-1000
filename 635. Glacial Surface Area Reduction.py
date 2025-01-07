def glacial_surface_area_reduction(initial_area = 500, rate = 0.02, years = 3):
    area=[initial_area]
    for i in range(years):
        area.append(area[-1]*(1-rate))
    return area

print(glacial_surface_area_reduction())