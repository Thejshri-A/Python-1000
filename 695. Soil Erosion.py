def soil_erosion(rainfall, soil_erodibility, slope_length, crop_cover,conservation):
    return rainfall*soil_erodibility*slope_length*crop_cover*conservation
rainfall=500
soil_erodibility = 0.3
slope_length = 2
crop_cover = 0.5
conservation = 0.9
print(soil_erosion(rainfall, soil_erodibility, slope_length, crop_cover, conservation))