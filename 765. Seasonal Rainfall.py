def seasonal_rainfall(rainfall = [50, 60, 45, 70, 80, 90, 120, 110, 100, 80, 60, 50]):
    winter=[rainfall[11],rainfall[0], rainfall[1]]
    spring=rainfall[2:5]
    summer=rainfall[5:8]
    fall=rainfall[8:11]
    seasons=[winter, spring, summer, fall]
    rainfall_trend=[]
    for season in seasons:
        rainfall_trend.append(sum(season)/len(season))
    return rainfall_trend

print(seasonal_rainfall())