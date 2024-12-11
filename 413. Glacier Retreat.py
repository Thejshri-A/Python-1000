def glacier_retreat(rate, years):
    return [rate*year for year in years]

rate = 5
years = [1, 2, 3, 4]
print(glacier_retreat(rate, years))