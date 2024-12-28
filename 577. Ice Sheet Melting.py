def ice_sheet_melting(initial_volume, melt_rate, years):
    volume=[initial_volume]
    for i in range(years):
        volume.append(volume[-1]-melt_rate)
    return volume

initial_volume = 1000
melt_rate = 50
years = 3
print(ice_sheet_melting(initial_volume, melt_rate, years))