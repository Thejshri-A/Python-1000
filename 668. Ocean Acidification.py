def ocean_acidification(initial_pH, rate, years):
    pH=[initial_pH]
    for i in range(years):
        pH.append(pH[-1]-rate)
    return pH

initial_pH = 8.1
rate = 0.01
years = 5
print(ocean_acidification(initial_pH, rate, years))
