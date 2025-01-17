def arabic_sea_ice_melt(initial_area = 1000, melt_rate = 50, years = 5):
    area=[initial_area]
    for i in range(years):
        area.append(area[-1]-melt_rate)
    return area

print(arabic_sea_ice_melt())