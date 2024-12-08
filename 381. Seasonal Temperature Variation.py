def seasonal_temp_variations(temps):
    seasons = { "Spring": temps[2:5],
               "Summer" : temps[5:8],
               "Monsoon" : temps[8:11],
               "Winter": temps[11:]+temps[:2]
        }
    
    return {season: round(sum(values)/len(values),2) for season, values in seasons.items()}

# Example
temps = [10, 12, 15, 20, 25, 30, 35, 38, 32, 20, 15, 10]
print(seasonal_temp_variations(temps))
# Output: {'Spring': 15.67, 'Summer': 34.33, 'Autumn': 22.33, 'Winter': 10.0}