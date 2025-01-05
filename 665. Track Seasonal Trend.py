def track_seasonal_trend(temperatures):
    seasons = {"Winter": [temperatures[11],temperatures[0],temperatures[1]],
               "Spring": temperatures[2:5],
               "Summer": temperatures[5:8],
               "Autumn": temperatures[8:11]}
    avg_temp = {season: sum(month)/len(month) for season, month in seasons.items()}
    highest_temps = max(avg_temp, key=avg_temp.get)
    return highest_temps

temperatures = [10, 15, 20, 25, 30, 35, 40, 35, 30, 25, 20, 15]
print(track_seasonal_trend(temperatures))