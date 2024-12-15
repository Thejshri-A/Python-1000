def seasonal_temperature_average(temps):
    seasons={
             "Winter": [temps[11],temps[0], temps[1]],
             "Spring": temps[2:5],
             "Summer": temps[5:8],
             "Monsoon": temps[8:11]
             }
    
    averages = {season: round(sum(months)/len(months),2) for season, months in seasons.items()}
    return averages

result = seasonal_temperature_average([2, 3, 7, 12, 15, 20, 25, 23, 19, 14, 8, 4])
print(result) 