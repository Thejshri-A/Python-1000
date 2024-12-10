def landslide_risk(rainfall, slope_angle, threshold):
    val = [r*s for r,s in zip(rainfall, slope_angle)]
    return sum(value>threshold for value in val)

rainfall = [100, 200, 150]
slope_angle = [10, 15, 20]
threshold = 2000
print(landslide_risk(rainfall, slope_angle, threshold))