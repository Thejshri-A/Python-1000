def model_co2(years, emissions):
    year=years[0]
    max_emission_diff=0
    
    for i in range(1, len(years)):
        emission_diff=emissions[i]-emissions[i-1]
        if emission_diff>max_emission_diff:
            max_emission_diff = emission_diff
            year=years[i-1]
    return year

years = [2000, 2001, 2002]
emissions = [4.2, 4.5, 4.9]
print(model_co2(years, emissions))