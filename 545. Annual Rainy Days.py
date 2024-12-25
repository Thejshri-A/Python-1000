def annual_rainy_days(rainfall):
    return sum(rain>1 for rain in rainfall)

rainfall = [0.5, 2.0, 1.5, 0.0, 3.0]
print(annual_rainy_days(rainfall))