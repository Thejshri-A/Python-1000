def seasonal_NDVI_averages(ndvi):
    seasons = {"Spring": ndvi[2:5],
               "Summer":ndvi[5:8],
               "Monsoon":ndvi[8:11],
               "Winter":ndvi[11:]+ndvi[:2]
               }
    
    return {season: round(sum(values)/len(values),2) for season, values in seasons.items()}
ndvi = [0.6, 0.7, 0.8, 0.9, 1.0, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]
print(seasonal_NDVI_averages(ndvi))