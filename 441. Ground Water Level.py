def ground_water(initial, final, years):
    return (initial-final)/years

initial = 50
final = 30
years = 5
print(ground_water(initial, final, years), " m/year")