def ice_sheet_melting(initial_volume, melt_rate, years):
    melting=[initial_volume]
    for i in range(years):
        melting.append(melting[-1]-melt_rate)
    return melting

initial_volume = 2000
melt_rate = 50
years = 3
print(ice_sheet_melting(initial_volume, melt_rate, years))
    