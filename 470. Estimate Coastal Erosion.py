def coastal_erosion(initial, erosion_rate, years):
    return f"Remaining Coastline : {initial - (erosion_rate*years)}"

initial = 1000
erosion_rate = 5
years = 10
print(coastal_erosion(initial, erosion_rate, years))