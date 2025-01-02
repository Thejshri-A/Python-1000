def deforestation_hotspot(forest_cover):
    return [i+1 for i in range(1, len(forest_cover)) if forest_cover[i]<forest_cover[i-1]]

forest_cover = [80, 75, 60, 50]
print(deforestation_hotspot(forest_cover))