def river_flood_probability(rainfall, saturation):
    return (rainfall*saturation)/100
rainfall = 50
saturation = 80
print(river_flood_probability(rainfall, saturation), "%")