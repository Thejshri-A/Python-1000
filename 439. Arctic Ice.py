def arctic_ice(ice_area, thickness):
    return [area*thick for area,thick in zip(ice_area, thickness)]

ice_area = [100, 120]
thickness = [2, 1.8]
print("Volume :", arctic_ice(ice_area, thickness))