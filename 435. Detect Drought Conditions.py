def detect_drought_conditions(years, rainfall, average):
    average_60_percent = 800*0.6
    
    return [y for y, r in zip(years, rainfall) if r<average_60_percent]
    
years = [2010, 2011]
rainfall = [600, 300]
average = 800

print("Drought conditions detected in ", detect_drought_conditions(years, rainfall, average))