def seasonal_rainfall(rainfall = [100, 50, 20, 200]):
    wettest = rainfall.index(max(rainfall))
    driest = rainfall.index(min(rainfall))
    return f"Wettest: {wettest}, Driest: {driest}"

print(seasonal_rainfall())